
class TV:
    def __init__(self, numero_canal, volume):
        pass
    
    def setNumero_canal(self, numero_canal):
        self.numero_canal = numero_canal
        
    def getNumero_canal(self):
        return self.numero_canal
    
    def setVolume(self, volume):
        self.volume = volume 
        
    def getVolume(self):
        return self.volume 
    
    def aumentarVolume(self, volume):
        return self.volume + 1 
    
    def diminuirVolume(self): 
        return self.volume - 1 
    
usuario = TV
usuario.setNumero_canal()
usuario.setVolume()
usuario.aumentarVolume()
usuario.diminuirVolume()
    
    