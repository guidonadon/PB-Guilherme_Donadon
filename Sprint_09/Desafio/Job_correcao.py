from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, explode, split, trim, monotonically_increasing_id

spark = SparkSession.builder.appName("Dim_GeneroArtista_Dim_Artista").getOrCreate()

imdb_df = spark.read.parquet("s3://datalake-pb-guilherme/Trusted/Movies/new/moviesseriescsv.parquet")

dim_genero_artista_df = imdb_df.select(
    explode(split(trim(col("profissao")), ",")).alias("genero_artista_nome")
).distinct().withColumn(
    "genero_artista_id", monotonically_increasing_id()
)

dim_artista_df = imdb_df.select(
    col("nomeArtista").alias("nome_artista"),
    col("anoNascimento").alias("ano_nascimento"),
    col("anoFalecimento").alias("ano_falecimento"),
    explode(split(trim(col("profissao")), ",")).alias("genero_artista_nome")
).join(
    dim_genero_artista_df,
    on="genero_artista_nome",
    how="left"
).select(
    "nome_artista",
    "ano_nascimento",
    "ano_falecimento",
    "genero_artista_nome",
    "genero_artista_id"
).distinct().withColumn(
    "id_artista", monotonically_increasing_id()
)

try:
    dim_genero_artista_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_GeneroArtista.parquet")
    print("Tabela Dim_GeneroArtista salva com sucesso no S3!")

    dim_artista_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_Artista.parquet")
    print("Tabela Dim_Artista salva com sucesso no S3!")
except Exception as e:
    print(f"Erro ao salvar as tabelas no S3: {e}")
