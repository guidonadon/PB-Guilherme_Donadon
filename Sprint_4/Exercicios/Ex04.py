def calcular_valor_maximo(operadores,operandos) -> float:
    def operacao(op, par):
        if op == '+':
            return par[0] + par[1]
        elif op == '-':
            return par[0] - par[1]
        elif op == '*':
            return par[0] * par[1]
        elif op == '/':
            return par[0] / par[1] if par [1] != 0 else float('inf')
        elif op == '%':
            return par[0] % par[1]
        else:
            raise ValueError(f'Operador desconhecido: {op}')
    
    juncao = zip(operadores, operandos)
    result = list(map(lambda x: operacao(x[0], x[1]), juncao))
    
    if result:
        return max(result)
    else:
        return float('-inf')
    
operandos = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
operadores = ['+', '-', '/', '*', '+']

print(calcular_valor_maximo(operadores, operandos))
