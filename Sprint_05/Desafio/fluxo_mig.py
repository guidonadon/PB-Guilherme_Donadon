import pandas as pd
import geopandas as gpd
import plotly.express as px
import pycountry
from googletrans import Translator
import boto3
from botocore.exceptions import ClientError
import tempfile

def download_from_s3(bucket_name, object_name, download_path):
    s3_client = boto3.client('s3')

    try:
        s3_client.download_file(bucket_name, object_name, download_path)
        print(f"Arquivo {object_name} baixado com sucesso para {download_path}.")
    except ClientError as e:
        print(f"Erro ao baixar arquivo: {e}")

bucket_name = "pb-bucket-guilherme"
object_name = "fluxo_migratorio.csv"
download_path = tempfile.gettempdir() + r"\fluxo_migratorio.csv"


download_from_s3(bucket_name, object_name, download_path)

df = pd.read_csv(download_path)

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

def get_country_code(country_name):
   
    custom_mapping = {
        "BOLÍVIA": "BOL",
        "BOLIVIA": "BOL",  
        "VENEZUELA": "VEN", 
        "RÚSSIA": "RUS",
        "RUSSIA": "RUS", 
        "COREIA DO SUL": "KOR", 
        "SOUTH KOREA": "KOR", 
    }

    if country_name in custom_mapping:
        return custom_mapping[country_name]

    try:
        country = pycountry.countries.get(name=country_name)
        return country.alpha_3 if country else None
    except KeyError:
        print(f"Não foi possível encontrar o código para o país: {country_name}")
        return None

df = pd.read_csv("fluxo_migratorio.csv")

df["NACIONALIDADE"] = df["NACIONALIDADE"].str.strip().str.upper() 
df["ANO"] = df["ANO"].astype(int)  

filtro = df["ANO"].between(2021, 2024)
df_filtrado = df[filtro]

agrupados_estados = (
    df_filtrado.groupby("UF_ATENDIMENTO")
    .agg(TOTAL_ATENDIMENTOS=("TOTAL", "sum"))
    .reset_index()
    .sort_values(by="TOTAL_ATENDIMENTOS", ascending=False)
    .reset_index(drop=True)  
)

top_estados = agrupados_estados.head(10)

top_paises = (
    df_filtrado[df_filtrado["NACIONALIDADE"] != "BRASIL"]
    .groupby("NACIONALIDADE")
    .agg(TOTAL=("TOTAL", "sum"))
    .reset_index()
    .sort_values(by="TOTAL", ascending=False)
    .reset_index(drop=True)  
    .head(30)
)

top_estados.index = top_estados.index + 1
top_paises.index = top_paises.index + 1

translator = Translator()

top_paises["NACIONALIDADE_INGLES"] = top_paises["NACIONALIDADE"].apply(lambda x: translator.translate(x, src='pt', dest='en').text)

top_paises["country_code"] = top_paises["NACIONALIDADE_INGLES"].apply(lambda x: get_country_code(x))

geo_estados = {
    'AC': (-8.7743, -70.5413), 'AL': (-9.5715, -36.7820), 'AP': (-0.9027, -52.0479),
    'AM': (-3.4161, -64.9355), 'BA': (-12.5791, -41.2849), 'CE': (-5.5467, -39.3206),
    'DF': (-15.7801, -47.9292), 'ES': (-20.3155, -40.3128), 'GO': (-16.6020, -49.2648),
    'MA': (-5.3659, -46.2967), 'MT': (-12.6376, -56.5024), 'MS': (-20.6510, -54.6012),
    'MG': (-18.5157, -44.2343), 'PA': (-5.8657, -52.2655), 'PB': (-7.1127, -35.2074),
    'PR': (-25.4284, -49.2733), 'PE': (-8.0476, -34.8770), 'PI': (-6.0034, -42.7036),
    'RJ': (-22.9068, -43.1729), 'RN': (-5.7945, -35.2110), 'RS': (-30.0346, -51.2177),
    'RO': (-10.8290, -63.7967), 'RR': (2.8007, -60.6693), 'SC': (-27.5954, -48.5480),
    'SP': (-23.5505, -46.6333), 'SE': (-10.9472, -37.0731), 'TO': (-10.1616, -48.2917)
}

top_estados = agrupados_estados.head(10).copy()
top_estados.loc[:, "LAT"] = top_estados["UF_ATENDIMENTO"].map(lambda x: geo_estados.get(x, (None, None))[0])
top_estados.loc[:, "LON"] = top_estados["UF_ATENDIMENTO"].map(lambda x: geo_estados.get(x, (None, None))[1])

try:
    brasil_map = gpd.read_file(r"C:/Users/guilh/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")
except Exception as e:
    print(f"Erro ao carregar o shapefile: {e}")
    brasil_map = None

if brasil_map is not None:
    brasil_map = brasil_map[brasil_map['NAME'] == 'Brazil']

    latitude_brasil = -14.2350  
    longitude_brasil = -51.9253  

    fig_br = px.scatter_geo(top_estados,
                            lat="LAT",
                            lon="LON",
                            size="TOTAL_ATENDIMENTOS",
                            hover_name="UF_ATENDIMENTO",
                            title="Top 10 Estados com maior números de Atendimentos (2021-2024)",
                            projection="mercator",
                            template="plotly",
                            color="TOTAL_ATENDIMENTOS",
                            color_continuous_scale="Viridis")
     
    scale_factor = 4
    fig_br.update_traces(marker=dict(sizemode='area', size=top_estados['TOTAL_ATENDIMENTOS'] * scale_factor))

    fig_br.update_geos(
        visible=True,  
        showcoastlines=True,  
        coastlinecolor="Black", 
        showland=True, 
        landcolor="Gainsboro",  
        projection_type="mercator",
        center={"lat": latitude_brasil, "lon": longitude_brasil}, 
        projection_scale=5  
    )
    fig_br.show()

try:
    world_map = gpd.read_file(r"C:/Users/guilh/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")
except Exception as e:
    print(f"Erro ao carregar o shapefile do mundo: {e}")
    world_map = None

if world_map is not None:
    fig_world = px.scatter_geo(top_paises,
                               locations="country_code",
                               size="TOTAL",
                               hover_name="NACIONALIDADE",
                               title="Top 30 Países com maiores fluxos migratórios no Brasil (2021-2024)",
                               projection="natural earth",
                               template="plotly",
                               color="TOTAL",
                               color_continuous_scale="Viridis")
    
    scale_factor = 3
    fig_world.update_traces(marker=dict(sizemode='area', size=top_paises['TOTAL'] * scale_factor))

    fig_world.update_geos(
        visible=True,  
        showcoastlines=True,  
        coastlinecolor="Gray",  
        showland=True,  
        landcolor="LightGray", 
    )

    fig_world.show()

top_estados.to_csv("top_10_atendimentos_BR.csv", index=False)
top_paises.to_csv("top_30_volume_mig.csv", index=False)

print("Top 10 estados com mais atendimentos (2021 a 2024) salvo em 'top_10_atendimentos_BR'.")
print("Top 30 países mais frequentes (excluindo BRASIL) salvo em 'top_30_volume_mig.csv'.")

output_file_1 = "top_10_atendimentos_BR.csv"
output_file_2 = "top_30_volume_mig.csv"

bucket_name = "pb-bucket-guilherme"
object_name_1 = "top_10_atendimentos_BR.csv"
object_name_2 = "top_30_volume_mig.csv"

create_bucket_if_not_exists(bucket_name)

upload_file_to_s3(output_file_1, bucket_name, object_name_1)
upload_file_to_s3(output_file_2, bucket_name, object_name_2)