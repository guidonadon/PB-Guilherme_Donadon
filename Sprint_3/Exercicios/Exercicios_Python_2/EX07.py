a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impar = []

for numero in a:
    if numero % 2 != 0:
        impar.append(numero)

print(impar)
