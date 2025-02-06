class Calculo:
    def soma(self, x, y):
        return x + y
        
    def subtracao(self, x, y):
        return x - y
        
x = 4
y = 5
Total = Calculo()

print(f'Somando: {x} + {y} = {Total.soma(x, y)}')
print(f'Subtraindo: {x} - {y} = {Total.subtracao(x, y)}')
