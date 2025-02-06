import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

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

data_atual = datetime.now().strftime("%Y/%m/%d")
pasta_arquivos = os.environ.get("DATA_DIR", "./data")
arquivos = {
    os.path.join(pasta_arquivos, "movies.csv"): f"Raw/Local/CSV/Movies/{data_atual}/",
    os.path.join(pasta_arquivos, "series.csv"): f"Raw/Local/CSV/Series/{data_atual}/"
}

bucket_name = "datalake-pb-guilherme"

create_bucket_if_not_exists(bucket_name)

for arquivo_local, pasta_s3 in arquivos.items():
    if os.path.exists(arquivo_local):
        nome_arquivo = os.path.basename(arquivo_local)
        chave_s3 = f"{pasta_s3}{nome_arquivo}"
        upload_file_to_s3(arquivo_local, bucket_name, chave_s3)
    else:
        print(f"Arquivo '{arquivo_local}' não foi encontrado.")