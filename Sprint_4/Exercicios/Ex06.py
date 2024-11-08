def maiores_que_media(conteudo:dict) -> list:
    preco_medio = sum(conteudo.values()) / len(conteudo)
    acima_media = filter(lambda item: item[1] > preco_medio, conteudo.items())
    produtos = sorted(acima_media, key=lambda item: item[1])
    return list(produtos)
    
itens = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(itens)
print (resultado)
