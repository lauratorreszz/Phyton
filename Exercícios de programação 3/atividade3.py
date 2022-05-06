
class Retangulo:
    def __init__(self, comprimento, largura):
        pass
    
    def setComprimento(self, comprimento):
        self.comprimento = comprimento
    
    def getComprimento(self):
        return self.comprimento
    
    def setLargura(self, largura):
        self.largura = largura 
        
    def getLargura(self):
        return self.largura 
    
    def mudarLados(self, comprimento, largura):
        pass
    
    def retornarLados(self):
        return self.mudarLados #?
    
    def calcularArea(self):
        return self.comprimento * self.largura
    
    def calcularPerimetro(self):
        return (self.comprimento*2) + (self.largura*2)
    
retangulo = Retangulo
retangulo.setComprimento()
retangulo.setLargura()
print(retangulo.calcularArea())
print(retangulo.calcularPerimetro())