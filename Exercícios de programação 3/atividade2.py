class Quadrado:

    def __init__(self,lado):
        pass
    
    def setLado(self,lado):
        self.lado = lado 
    
    def getLado(self):
        return self.lado
    
    def calcularArea(self):
        return self.lado * self.lado 

quadrado = Quadrado 
quadrado.setLado()
print(quadrado.calcularArea())