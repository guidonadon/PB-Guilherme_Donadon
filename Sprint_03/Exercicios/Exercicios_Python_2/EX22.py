class Pessoa:
    def __init__(self, nome):
        self.__nome = None
    
    def id(self):
        self.id = id
    
    def nome(self):
        return self.__nome
    
pessoa = Pessoa(0)
pessoa.nome = 'Fulano de Tal'
print(pessoa.nome)
