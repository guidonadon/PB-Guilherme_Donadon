class Aviao:
  def __init__(self, modelo, velocidade, capacidade):
    self.modelo = modelo
    self.velocidade = velocidade 
    self.capacidade = capacidade
    self.cor = 'Azul'

listaaviao = []
listaaviao2 = []
listaaviao3 = []
listaaviao.append(Aviao('BOIENG456','1500Km/h','400'))
listaaviao2.append(Aviao('Embraer Praetor 600','863km/h','14'))
listaaviao3.append(Aviao('Antonov An-2','258km/h','12'))

for Aviao in listaaviao:
  print(f'O avião de modelo {Aviao.modelo} possui um velocidade máxima de {Aviao.velocidade}, capacidade para {Aviao.capacidade} passageiros e é da cor {Aviao.cor}')

for Aviao in listaaviao2:
  print(f'O avião de modelo {Aviao.modelo} possui um velocidade máxima de {Aviao.velocidade}, capacidade para {Aviao.capacidade} passageiros e é da cor {Aviao.cor}')

for Aviao in listaaviao3:
  print(f'O avião de modelo {Aviao.modelo} possui um velocidade máxima de {Aviao.velocidade}, capacidade para {Aviao.capacidade} passageiros e é da cor {Aviao.cor}')
