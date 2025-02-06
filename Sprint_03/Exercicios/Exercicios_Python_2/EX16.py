numeros_txt = "1,3,4,6,10,76"
numeros = [int(num) for num in numeros_txt.split(',')]
total = sum(numeros)
print(total)
