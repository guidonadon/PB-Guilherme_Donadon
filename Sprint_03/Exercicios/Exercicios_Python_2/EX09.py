primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

info_completas = [list(dados) for dados in zip(primeirosNomes, sobreNomes, idades)]

for i, (primeirosNomes, sobreNomes, idades) in enumerate(info_completas):
    print(f"{i} - {primeirosNomes} {sobreNomes} está com {idades} anos")
