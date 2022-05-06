
class Conta:
    def  __init__(self, numero, nome, saldo ):
        pass
    
    #a ordem importa? 
    def setNome(self, nome):
        self.nome = nome 
        
    def getNome(self):
        return self.nome
    
    def setNumero(self, numero):
        self.numero = numero
        
    def getNumero(self):
        return self.numero
    
    def setSaldo(self, saldo):
        self.saldo = saldo
        
    def getSaldo(self):
        return self.saldo
    
    def alterarNome(self, nome ):
        pass 
        
    def depositar(self, saldo):
        pass
    
    def saque(self): 
        pass
        
correntista = Conta 
correntista.setNome()
correntista.setNumero()
correntista.setSaldo()
correntista.alterarNome()
correntista.depositar()
correntista.saque()
