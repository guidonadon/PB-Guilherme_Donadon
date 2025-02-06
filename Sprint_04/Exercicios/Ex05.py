import csv

def notas_alunos(arquivo_csv):
    with open(arquivo_csv, 'r') as estudantes:
        leitor = csv.reader(estudantes)
        alunos = [linha for linha in leitor]
    
    dados = []
    for aluno in alunos:
        nome = aluno[0]
        notas = list(map(float, aluno[1:]))
        top3 = sorted(notas, reverse=True)[:3]
        media_notas = round(sum(top3) / 3, 2)
        dados.append((nome, top3, media_notas))
        
    dados_ordenados = sorted(dados, key=lambda x: x[0])
    
    for nome, notas, media_notas in dados_ordenados:
        notas_formatadas = [str(int(n)) for n in notas]

        if media_notas == int(media_notas):
            media_formatada = f'{media_notas:.1f}'
        else:
            media_formatada = f'{media_notas:.2f}'

        print(f'Nome: {nome} Notas: [{", ".join(notas_formatadas)}] Média: {media_formatada}')

notas_alunos('estudantes.csv')
