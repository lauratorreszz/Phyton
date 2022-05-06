class Quadrado:
    
    #funçoes em class sempre tem self para atribuir ao, nesse caso, quadrado
    #função de inicialização, sempre primeiro a ser definido em uma classe e smp vai ter 
    def __init__(self,lado):
        pass
    
    #para inserir os lados 
    def setLado(self,lado):
        self.lado = lado 
    
    #sistema pega os lados 
    def getLado(self):
        return self.lado
    
    def calculaArea(self):
        return self.lado * self.lado 

quadrado = Quadrado 
print(quadrado.calculaArea())