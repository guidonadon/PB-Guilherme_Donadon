with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
top5 = sorted(numeros_pares, reverse=True)[:5]
soma_pares = sum(top5)

print(top5)
print(soma_pares)
