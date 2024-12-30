import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper
from pyspark.sql.functions import col, sum as _sum

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_input_path = "s3://ex-glue-pb-guilherme/lab-glue/input/nomes.csv"

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [s3_input_path]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
)

print("Schema do DataFrame:")
df_spark = df.toDF()

df_spark = df_spark.withColumn("nome", upper(df_spark["nome"]))
print("O total de linhas no DataFrame é:", df_spark.count())

AnoSexo = (
    df_spark.groupBy("ano", "sexo")
    .count()
    .orderBy("ano", ascending=False)
)
AnoSexo.show()

mulheres = (
    df_spark.filter(col("sexo") == "F")
    .groupBy("nome", "ano")
    .agg(_sum("total").alias("reg_fem"))
    .orderBy(col("reg_fem").desc())
    .first()
)
print(
    f"O nome feminino mais popular é: {mulheres['nome']}, No ano: {mulheres['ano']}, com o número de registros de: {mulheres['reg_fem']}"
)

homens = (
    df_spark.filter(col("sexo") == "M")
    .groupBy("nome", "ano")
    .agg(_sum("total").alias("reg_masc"))
    .orderBy(col("reg_masc").desc())
    .first()
)
print(
    f"O nome masculino mais popular é: {homens['nome']}, No ano: {homens['ano']}, com o número de registros de: {homens['reg_masc']}"
)

total_anual = (
    df_spark.groupBy("ano")
    .agg(_sum("total").alias("total_reg"))
    .orderBy("ano", ascending=True)
)
total_anual.show(10)

output_path = "s3://ex-glue-pb-guilherme/lab-glue/frequencia_registro_nomes_eua"
df_spark.write.mode("overwrite").format("json").partitionBy("sexo", "ano").save(output_path)

print("O arquivo foi salvo com sucesso em seu bucket S3!!")

job.commit()
