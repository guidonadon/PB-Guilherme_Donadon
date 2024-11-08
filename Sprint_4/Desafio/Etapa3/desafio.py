import hashlib

while True:
    nova_hash = hashlib.sha1()
    incognita = input('Qual sua hash oculta? Digite seu nome: ')
    
    nova_hash.update(incognita.encode())
    nova_hash.digest()
    print(nova_hash.hexdigest())

    Resultado = input('Deseja finalizar? Digite [S] ou [N]: ').upper()
    if Resultado == 'S':
        break
    else:
        continue