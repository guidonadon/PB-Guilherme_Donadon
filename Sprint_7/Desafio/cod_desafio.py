import boto3
import requests
import json
import os
import csv
from io import StringIO
import random

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

headers = {
    "Authorization": f"Bearer {TMDB_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

s3_client = boto3.client('s3')
{
  "bucket_name": "datalake-pb-guilherme",
  "movies_key": "s3://datalake-pb-guilherme/Raw/Local/CSV/Movies/2024/12/09/movies.csv",
  "series_key": "s3://datalake-pb-guilherme/Raw/Local/CSV/Series/2024/12/09/series.csv",
  "output_folder": "s3://datalake-pb-guilherme/Raw/API_TMDB/"
}


def amostragem_anual(movies_data, coluna_ano, generos_aceitos):
    if coluna_ano not in movies_data[0]:
        raise ValueError(f"A coluna '{coluna_ano}' não foi encontrada nos dados.")
    
    movies_data = [movie for movie in movies_data if movie['genero'] in generos_aceitos]
    
    movies_data = [movie for movie in movies_data if movie.get(coluna_ano)]

    grouped = {}
    for movie in movies_data:
        ano = movie[coluna_ano]
        if ano not in grouped:
            grouped[ano] = []
        grouped[ano].append(movie)
    
    amostra = []
    for ano, movies in grouped.items():
        amostra.extend(random.sample(movies, 3))
    
    return amostra

def buscar_producoes(imdb_id):
    url = f"https://api.themoviedb.org/3/find/{imdb_id}"
    params = {"api_key": TMDB_TOKEN, "external_source": "imdb_id"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'movie_results' in data and data['movie_results']:
            return data['movie_results'][0]
        elif 'tv_results' in data and data['tv_results']:
            return data['tv_results'][0]
        else:
            print(f"Nenhum resultado encontrado para o ID {imdb_id}")
            return None
    else:
        print(f"Erro ao buscar ID {imdb_id}: {response.status_code}")
        return None

def complementos(movies_data):
    dados_complementares = []
    for movie in movies_data:
        imdb_id = movie["id"]
        dados_tmdb = buscar_producoes(imdb_id)
        if dados_tmdb:
            dados_complementares.append(dados_tmdb)
    return dados_complementares

def dividir_em_lotes(dados, tamanho_lote=100):
    return [dados[i:i + tamanho_lote] for i in range(0, len(dados), tamanho_lote)]

def ler_csv_do_s3(bucket, key):
    response = s3_client.get_object(Bucket=bucket, Key=key)
    csv_content = response["Body"].read().decode("utf-8")
    csv_reader = csv.DictReader(StringIO(csv_content), delimiter='|')
    return [row for row in csv_reader]

def salvar_json_no_s3(bucket, key, data):
    json_content = json.dumps(data, indent=4)
    s3_client.put_object(Bucket=bucket, Key=key, Body=json_content)

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    movies_key = event['movies_key']
    series_key = event['series_key']
    output_folder = event['output_folder']
    
    movies_data = ler_csv_do_s3(bucket_name, movies_key)
    series_data = ler_csv_do_s3(bucket_name, series_key)
    
    generos_aceitos = ['Action', 'Adventure']
    
    amostras_movies = amostragem_anual(movies_data, "anoLancamento", generos_aceitos)
    amostras_series = amostragem_anual(series_data, "anoLancamento", generos_aceitos)
    
    print("Processando filmes...")
    dados_filmes = complementos(amostras_movies)
    lotes_filmes = dividir_em_lotes(dados_filmes)
    
    for idx, lote in enumerate(lotes_filmes, 1):
        output_key = f"{output_folder}dados_filmes_{idx}.json"
        salvar_json_no_s3(bucket_name, output_key, lote)
        print(f"Lote de filmes {idx} salvo com sucesso no S3!")
    
    print("Processando séries...")
    dados_series = complementos(amostras_series)
    lotes_series = dividir_em_lotes(dados_series)
    
    for idx, lote in enumerate(lotes_series, 1):
        output_key = f"{output_folder}dados_series_{idx}.json"
        salvar_json_no_s3(bucket_name, output_key, lote)
        print(f"Lote de séries {idx} salvo com sucesso no S3!")

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
