numeros = list(range(1, 101))

def primos(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for numero in numeros:    
    if primos(numero):
        print (numero)
