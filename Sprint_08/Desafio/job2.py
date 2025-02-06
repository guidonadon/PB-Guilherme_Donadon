from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from pyspark.sql.functions import col, lit, when, size
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, FloatType, BooleanType

sc = SparkContext()
spark = SparkSession(sc)
glueContext = GlueContext(sc)

schema = StructType([
    StructField("name", StringType(), True),
    StructField("original_name", StringType(), True),
    StructField("overview", StringType(), True),
    StructField("first_air_date", StringType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", FloatType(), True),
    StructField("popularity", FloatType(), True),
    StructField("media_type", StringType(), True),
    StructField("adult", BooleanType(), True),
    StructField("original_language", StringType(), True),
    StructField("backdrop_path", StringType(), True),
    StructField("poster_path", StringType(), True),
    StructField("origin_country", ArrayType(StringType()), True),
    StructField("genre_ids", ArrayType(StringType()), True),
])

tmdb_data_path = "s3://datalake-pb-guilherme/Raw/API_TMDB/"
tmdb_df = spark.read.schema(schema).json(tmdb_data_path)

movies_df = spark.read.schema(schema).json("s3://datalake-pb-guilherme/Raw/API_TMDB/dados_filmes_1.json")
movies_df = movies_df.union(spark.read.schema(schema).json("s3://datalake-pb-guilherme/Raw/API_TMDB/dados_filmes_2.json"))
movies_df = movies_df.union(spark.read.schema(schema).json("s3://datalake-pb-guilherme/Raw/API_TMDB/dados_filmes_3.json"))

series_df = spark.read.schema(schema).json("s3://datalake-pb-guilherme/Raw/API_TMDB/dados_series_1.json")
series_df = series_df.union(spark.read.schema(schema).json("s3://datalake-pb-guilherme/Raw/API_TMDB/dados_series_2.json"))

def fill_missing_values(df):
    if "origin_country" not in df.columns:
        df = df.withColumn("origin_country", lit(["desconhecido"]))
    else:
        df = df.withColumn(
            "origin_country",
            when(
                (col("origin_country").isNull()) | (size(col("origin_country")) == 0),
                lit(["desconhecido"])
            ).otherwise(col("origin_country"))
        )

    if "genre_ids" not in df.columns:
        df = df.withColumn("genre_ids", lit(["Desconhecido"]))
    else:
        df = df.withColumn(
            "genre_ids",
            when(
                (col("genre_ids").isNull()) | (size(col("genre_ids")) == 0),
                lit(["Desconhecido"])
            ).otherwise(col("genre_ids"))
        )
    
    columns_to_fill = {
        "name": "Desconhecido",
        "original_name": "Desconhecido",
        "overview": "Sem descrição",
        "first_air_date": "1900-01-01",
        "vote_average": 0.0,
        "vote_count": 0,
        "popularity": 0.0,
        "media_type": "Desconhecido",
        "adult": False,
        "original_language": "Desconhecido",
        "backdrop_path": "Desconhecido",
        "poster_path": "Desconhecido"
    }

    for col_name, default_value in columns_to_fill.items():
        if col_name not in df.columns:
            df = df.withColumn(col_name, lit(default_value))
        else:
            df = df.fillna({col_name: default_value})
    
    return df

movies_df = fill_missing_values(movies_df)
series_df = fill_missing_values(series_df)

movies_df = movies_df.withColumn("data_criacao", lit("2024-12-09"))
series_df = series_df.withColumn("data_criacao", lit("2024-12-09"))

trusted_movies_path = "s3://datalake-pb-guilherme/Trusted/TMDB/movies/"
trusted_series_path = "s3://datalake-pb-guilherme/Trusted/TMDB/series/"

movies_df.write.mode("overwrite").partitionBy("data_criacao").parquet(trusted_movies_path)
series_df.write.mode("overwrite").partitionBy("data_criacao").parquet(trusted_series_path)

print("Processamento dos dados da API TMDB concluído com sucesso!")
