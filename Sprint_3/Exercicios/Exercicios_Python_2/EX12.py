lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_map(list, f):
    saída = [f(termo) for termo in lista]
    return saída
    
def potencia(numero):
    return numero ** 2

lista_nova = my_map(lista, potencia)

print (lista_nova)
