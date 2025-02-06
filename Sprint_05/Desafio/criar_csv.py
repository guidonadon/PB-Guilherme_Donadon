import polars as pl
import os
import boto3
from botocore.exceptions import ClientError

def create_bucket_if_not_exists(bucket_name, region="us-east-1"):
    s3_client = boto3.client('s3', region_name=region)
    
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} já existe.")
    except ClientError:
        print(f"Bucket {bucket_name} não encontrado, criando novo bucket.")
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} criado com sucesso.")

def upload_file_to_s3(file_path, bucket_name, object_name):
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Arquivo {object_name} enviado para o bucket {bucket_name} com sucesso.")
    except ClientError as e:
        print(f"Erro ao enviar o arquivo: {e}")

pasta_arquivos = r"C:\Users\guilh\OneDrive\Documentos\Compass\Sprint5\desafio"
arquivos = [os.path.join(pasta_arquivos, f) for f in os.listdir(pasta_arquivos) if f.endswith(".csv")]

dataframes = []

for arquivo in arquivos:
    nome_base = os.path.basename(arquivo)
    partes = nome_base.split("_")
    ano = partes[2]
    mes = partes[3].replace(".csv", "")

    df = pl.read_csv(
        arquivo,
        encoding="ISO-8859-1",
        separator=";",
        schema={
            "UF_ATENDIMENTO": pl.Utf8,
            "TIPO": pl.Utf8,
            "CLASSIFICACAO": pl.Utf8,
            "NACIONALIDADE": pl.Utf8,
            "TOTAL": pl.Int64,
        },
        null_values=["#####"]
    )
    
    df = df.with_columns([
        pl.lit(int(ano)).alias("ANO"),
        pl.lit(int(mes)).alias("MES")
    ])
    
    dataframes.append(df)

dados_unificados = pl.concat(dataframes)

output_file = "fluxo_migratorio.csv"
dados_unificados.write_csv(output_file)

bucket_name = "pb-bucket-guilherme"
object_name = "fluxo_migratorio.csv"

create_bucket_if_not_exists(bucket_name)

upload_file_to_s3(output_file, bucket_name, object_name)