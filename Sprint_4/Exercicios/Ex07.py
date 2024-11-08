def pares_ate(n:int):
    for numero in range(2, n + 1):
        if numero % 2 ==0:
            yield numero

for par in pares_ate(10):
    print(par)
