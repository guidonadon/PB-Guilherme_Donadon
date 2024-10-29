lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

tam_lista = len(lista) // 3

lista1 = lista[:tam_lista]
lista2 = lista[tam_lista:2 * tam_lista]
lista3 = lista[2 * tam_lista:]

print(f'{lista1} {lista2} {lista3}')
