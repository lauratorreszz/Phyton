
class Tamagushi:
    def __init__(self, nome,idade):
        pass
    
    def setNome(self, nome):
        self.nome = nome 
        
    def getNome(self):
        return self.nome
    
        
    def getIdade(self):
        return self.idade 
    
    def setPeso(self, peso):
        self.peso = peso
        
    def getPeso(self):
        return self.peso
    
    def setAltura(self, altura ):
        self.altura = altura
        
    def getAltura(self):
        return self.altura
    
    def envelhecer(self, idade):
        pass
    
    def engordar(self, peso):
        pass
    
    def humor(self, fome, saude):
        self.fome = fome 
        self.saude = saude 
        self.humor = self.fome + self.saude 
        
tamagushi = Tamagushi 
tamagushi.setNome()
tamagushi.setAltura()
tamagushi.setPeso()
tamagushi.engordar()
tamagushi.envelhecer()
tamagushi.humor()
