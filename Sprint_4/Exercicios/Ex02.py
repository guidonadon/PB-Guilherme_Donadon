def conta_vogais(texto:str)-> int:
    vogais = "aeiouAEIOU"
    vogais_presentes = filter(lambda char: char in vogais, texto)
    return len(list(vogais_presentes))

print(conta_vogais(""))
