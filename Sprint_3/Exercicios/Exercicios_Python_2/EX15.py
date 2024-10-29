class Lampada:
    def __init__(self, inicio):
        self.ligada = inicio
        
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada
        
luz = Lampada(False)

luz.liga()
print('A luz está ligada?', luz.esta_ligada())

luz.desliga()
print('A luz está ligada?', luz.esta_ligada())
