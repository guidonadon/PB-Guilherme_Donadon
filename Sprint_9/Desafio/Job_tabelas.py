from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import col, lit, explode, split, trim, monotonically_increasing_id, when

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

imdb_df = spark.read.parquet("s3://datalake-pb-guilherme/Trusted/Movies/new/moviesseriescsv.parquet")
movies_tmdb_df = spark.read.parquet("s3://datalake-pb-guilherme/Trusted/TMDB/movies/new/movies_corrigido.parquet")
series_tmdb_df = spark.read.parquet("s3://datalake-pb-guilherme/Trusted/TMDB/series/new/series_corrigido.parquet")

movies_tmdb_df = movies_tmdb_df.withColumn("media_type", lit("movie"))
series_tmdb_df = series_tmdb_df.withColumn("media_type", lit("tv"))

tmdb_df = movies_tmdb_df.select(
    col("id").alias("id_film_series"),
    col("title").alias("titulo_principal"),
    col("original_title").alias("titulo_original"),
    col("overview").alias("descricao"),
    col("release_date").alias("data_lancamento"),
    col("backdrop_path").alias("imagem_url"),
    col("original_language").alias("idioma"),
    col("media_type")
).union(
    series_tmdb_df.select(
        col("id").alias("id_film_series"),
        col("name").alias("titulo_principal"),
        col("original_name").alias("titulo_original"),
        col("overview").alias("descricao"),
        col("first_air_date").alias("data_lancamento"),
        col("backdrop_path").alias("imagem_url"),
        col("original_language").alias("idioma"),
        col("media_type")
    )
)

tmdb_df = tmdb_df.withColumn(
    "imagem_url",
    when(col("imagem_url").isNull(), "desconhecido").otherwise(col("imagem_url"))
).withColumn(
    "idioma",
    when(col("idioma").isNull(), "desconhecido").otherwise(col("idioma"))
)

dim_film_series_df = tmdb_df.select(
    col("id_film_series"),
    col("titulo_principal"),
    col("titulo_original"),
    col("descricao"),
    col("data_lancamento"),
    col("media_type"),
    col("imagem_url"),
    col("idioma")
).distinct()

dim_genero_df = imdb_df.select(
    explode(split(col("genero"), ",")).alias("genero_nome")
).distinct().withColumn(
    "genero_id", monotonically_increasing_id()
)

dim_artista_df = imdb_df.select(
    col("nomeArtista").alias("nome_artista"),
    col("anoNascimento").alias("ano_nascimento"),
    col("anoFalecimento").alias("ano_falecimento"),
    col("profissao").alias("genero_artista_nome")
).distinct().withColumn(
    "id_artista", monotonically_increasing_id()
)

dim_genero_artista_df = imdb_df.select(
    col("profissao").alias("genero_artista_nome")
).distinct().withColumn(
    "genero_artista_id", monotonically_increasing_id()
)

dim_film_artista_df = imdb_df.select(
    col("id").alias("id_film_series"),
    col("nomeArtista"),
    col("personagem").alias("papel")
).join(
    dim_artista_df,
    imdb_df["nomeArtista"] == dim_artista_df["nome_artista"],
    "left"
).select(
    "id_film_series",
    dim_artista_df["nome_artista"],
    "papel"
).distinct()

fact_movies_series_df = imdb_df.select(
    col("id").alias("id_film_series"),
    col("notaMedia").alias("nota_media"),
    col("numeroVotos").alias("numero_votos"),
    col("anoLancamento").alias("ano_lancamento"),
    col("genero"),
    col("nomeArtista")
).join(
    dim_genero_df,
    col("genero") == dim_genero_df["genero_nome"],
    "left"
).join(
    dim_artista_df,
    col("nomeArtista") == dim_artista_df["nome_artista"],
    "left"
).select(
    monotonically_increasing_id().alias("id_fato"),
    "id_film_series",
    "nota_media",
    "numero_votos",
    "ano_lancamento",
    "genero_id",
    "id_artista"
)

try:
    dim_film_series_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_FilmSeries.parquet")
    dim_genero_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_Genero.parquet")
    dim_artista_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_Artista.parquet")
    dim_genero_artista_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_GeneroArtista.parquet")
    dim_film_artista_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Dim_FilmArtista.parquet")
    fact_movies_series_df.write.mode("overwrite").parquet("s3://datalake-pb-guilherme/Refined/Fact_MoviesSeries.parquet")
    print("Tabelas salvas com sucesso no S3!")
except Exception as e:
    print(f"Erro ao gravar os arquivos Parquet: {e}")
