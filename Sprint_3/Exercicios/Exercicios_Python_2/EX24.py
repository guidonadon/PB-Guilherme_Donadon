class Ordenadora:
  def __init__(self,listaBaguncada):
    self.listaBaguncada = listaBaguncada

  def ordenacaoCrescente(self):
      return sorted(self.listaBaguncada)

  def ordenacaoDecrescente(self):
      return sorted(self.listaBaguncada)[::-1]

lista1 = Ordenadora([3,4,2,1,5])
lista2 = Ordenadora([9,7,6,8])

print(lista1.ordenacaoCrescente())
print(lista2.ordenacaoDecrescente())
