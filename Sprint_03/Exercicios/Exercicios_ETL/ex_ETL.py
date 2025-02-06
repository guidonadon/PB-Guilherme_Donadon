#! python

with open('actors.csv', 'r') as atores_filmes:
    amostra = [linha.strip().split(',') for linha in atores_filmes]

maior = 0
ator = ''
receita_total = 0
media_ator = 0
ator_mais_rico = ''
n_filmes = 0
contagem_filmes = {}
receita_bruta_ator = {}

for coluna in amostra[1:]:
    filmes = int(coluna[-4])
    if filmes > maior:
        maior = filmes
        ator = coluna[0]

with open('Etapa-1.txt', 'w', encoding='utf-8') as resultado:
    resultado.write('Apresente o ator/atriz com maior número de filmes e a respectiva quantidade:')
    resultado.write('\n Ator com mais filmes: {}, quantidade de filmes: {}.'.format(ator, maior))
    resultado.close()

for coluna in amostra[1:]:
    gross = float(coluna[-1])
    receita_total += gross
    n_filmes += 1
receita_media = receita_total / n_filmes
with open('Etapa-2.txt', 'w', encoding='utf-8') as resultado:
        resultado.write(f'Receita média de bilheteria dos principais filmes, considerando todos os atores.')    
        resultado.write(f'\n Média de receita de {n_filmes} filmes: {receita_media:.2f}')

for coluna in amostra[1:]:
    ator = coluna[0]
    maior_media = float(coluna[-3].strip())
    if maior_media > media_ator:
        media_ator = maior_media
        ator_mais_rico = ator
with open('Etapa-3.txt', 'w', encoding='utf-8') as resultado:
    resultado.write(f'Ator/Atriz com maior média de faturamento: {ator_mais_rico} possui média de faturamento bruto: {media_ator}\n')

for coluna in amostra[1:]:
    filme = coluna[-2]
    if filme in contagem_filmes:
        contagem_filmes[filme] += 1
    else:
        contagem_filmes[filme] = 1
lista_filmes = sorted(contagem_filmes.items(), key=lambda x: x[1], reverse=True)
with open('Etapa-4.txt', 'w', encoding='utf-8') as resultado:
    for posicao, (filme, contagem) in enumerate(lista_filmes, start=1):
        resultado.write(f'{posicao} - O filme {filme} aparece {contagem} vezes no dataset.\n')

for coluna in amostra[1:]:
    ator= coluna[0]
    if ', Jr.' in ator:
        ator = ator.replace(', Jr.', ' Jr.')
    salario_ator = float(coluna[-5])
    if ator in receita_bruta_ator:
        receita_bruta_ator[ator] += salario_ator
    else:
        receita_bruta_ator[ator] = salario_ator
lista_atores = sorted(receita_bruta_ator.items(), key=lambda x: x[1], reverse=True)
with open('Etapa-5.txt', 'w', encoding='utf-8') as resultado:
    for ator, salario in lista_atores:
        resultado.write(f'{ator} - {salario:.2f}\n')