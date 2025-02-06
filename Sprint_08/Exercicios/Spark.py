# Etapa 1
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, rand, floor

spark = SparkSession.builder \
    .appName("Exercicio Intro") \
    .master("local[*]") \
    .getOrCreate()

df_nomes = spark.read.csv("/home/jovyan/work/Nomes_aleatorios.txt", header=True, inferSchema=True)

df_nomes.show(10)

# Etapa 2
df_nomes = df_nomes.withColumnRenamed("nome", "Nomes")

df_nomes.printSchema()
df_nomes.show(10)

# Etapa 3
escolaridades = ["Fundamental", "Medio", "Superior"]
df_nomes = df_nomes.withColumn("Escolaridade", lit(escolaridades).getItem((rand() * 3).cast("int")))

# Etapa 4
paises = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador", "Paraguai", "Peru", "Uruguai", "Venezuela"]
df_nomes = df_nomes.withColumn("Pais", lit(paises).getItem((rand() * len(paises)).cast("int")))

# Etapa 5
df_nomes = df_nomes.withColumn("AnoNascimento", (floor(rand() * (2010 - 1945 + 1)) + 1945).cast("int"))

df_nomes.show(10)

# Etapa 6
df_select = df_nomes.filter(col("AnoNascimento") >= 2000)

df_select.show(10)

# Etapa 7
df_nomes.createOrReplaceTempView("nomes")

df_select_sql = spark.sql("SELECT * FROM nomes WHERE AnoNascimento >= 2000")

df_select_sql.show(10)

# Etapa 8
millennials_count = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print(f"Quantidade de Millennials: {millennials_count}")

# Etapa 9
millennials_count_sql = spark.sql("SELECT COUNT(*) AS Millennials FROM nomes WHERE AnoNascimento BETWEEN 1980 AND 1994")
millennials_count_sql.show()

# Etapa 10
df_nomes = df_nomes.withColumnRenamed("País", "Pais")

df_nomes.createOrReplaceTempView("nomes")

geracoes_query = """
SELECT 
    Pais,
    CASE 
        WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
        WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
    END AS Geracao,
    COUNT(*) AS Quantidade
FROM nomes
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao
"""

df_geracoes = spark.sql(geracoes_query)

df_geracoes.show()