import random
import names
import time
import os

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

inicio = time.time()

aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())
print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios!")

dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

pasta_atual = os.getcwd()
arquivo_nome = os.path.join(pasta_atual, "Nomes_aleatorios.txt")

with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(dados))

fim = time.time()

print(f"Os nomes aleatórios foram gerados e salvos com sucesso no arquivo: {arquivo_nome}!")
print(f"O tempo de execução do script foi de {fim - inicio:.2f} segundos.")