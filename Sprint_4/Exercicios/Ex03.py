from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C'
        else -x[0], lancamentos)
    
    saldo = reduce(lambda x, y: x+ y, valores)
    return saldo
    
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))
