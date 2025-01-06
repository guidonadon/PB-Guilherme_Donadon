import sys
import boto3
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext

sc = SparkContext()
spark = SparkSession(sc)
glueContext = GlueContext(sc)

movies_path = "s3://datalake-pb-guilherme/Raw/Local/CSV/Movies/2024/12/09/movies.csv"
series_path = "s3://datalake-pb-guilherme/Raw/Local/CSV/Series/2024/12/09/series.csv"

movies_df = spark.read.csv(movies_path, header=True, inferSchema=True, sep="|")
series_df = spark.read.csv(series_path, header=True, inferSchema=True, sep="|")

movies_df = movies_df.replace("\\N", None).fillna({
    'genero': 'Desconhecido',
    'anoNascimento': 'Desconhecido',
    'anoFalecimento': 'Desconhecido',
    'notaMedia': 0
})
series_df = series_df.replace("\\N", None).fillna({
    'genero': 'Desconhecido',
    'anoNascimento': 'Desconhecido',
    'anoFalecimento': 'Desconhecido',
    'notaMedia': 0
})

trusted_movies_path = "s3://datalake-pb-guilherme/Trusted/Movies/"
trusted_series_path = "s3://datalake-pb-guilherme/Trusted/Series/"

movies_df.write.mode("overwrite").parquet(trusted_movies_path)
series_df.write.mode("overwrite").parquet(trusted_series_path)

catalog_database = "desafio-pb-guilherme-database"
movies_table = "movies_csv"
series_table = "series_csv"

movies_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database=catalog_database, table_name=movies_table
)
series_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database=catalog_database, table_name=series_table
)

print("Esquema Movies:")
movies_dynamic_frame.printSchema()
print("Esquema Series:")
series_dynamic_frame.printSchema()

print("Job executado com sucesso. Dados salvos no S3 e carregados no Glue Catalog.")
