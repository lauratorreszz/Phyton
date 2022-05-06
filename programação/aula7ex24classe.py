class Pessoa:
    def __init__(self, nome, idade, trabalho, estado_civil, cpf, rg):
        pass
    
    def setNome(self, nome):
        self.nome = nome 
        
    def getNome(self):
        return self.nome
    
    def setIdade(self, idade):
        self.idade = idade
        
    def getIdade(self):
        return self.idade 
    
    def setTrabalho(self, trabalho):
        self.trabalho = trabalho
        
    def getTrabalho(self):
        return self.trabalho
    
    def setEstadoCIVIL(self, estado_civil ):
        self.estado_civil = estado_civil
        
    def getEstadoCIVIL(self):
        return self.estado_civil
    
    def setCPF(self, cpf):
        self.cpf = cpf
        
    def getCPF(self):
        return self.cpf
    
    def setRG(self, rg):
        self.rg = rg
        
    def getRG(self):
        return self.rg 
    
pessoa = Pessoa()
pessoa.setNome()
pessoa.setIdade()
pessoa.setTrabalho()
pessoa.setEstadoCIVIL()
pessoa.setCPF()
pessoa.setRG()
    
    
class Academia:
    def __init__(self, nome, idade, telefone, plano, saude):
        pass
    
    def setNome(self, nome):
        self.nome = nome 
        
    def getNome(self):
        return self.nome
    
    def setIdade(self, idade):
        self.idade = idade
        
    def getIdade(self):
        return self.idade 
    
    def setTelefone(self, telefone):
        self.telefone = telefone
        
    def getTelefone(self):
        return self.telefone
    
    def setPlano(self, plano ):
        self.plano = plano
        
    def getPlano(self):
        return self.plano
    
    def setSaude(self, saude):
        self.saude = saude
        
    def getSaude(self):
        return self.saude
    
    
ficha_cliente = Academia()
ficha_cliente.setNome()
ficha_cliente.setIdade()
ficha_cliente.setTelefone()
ficha_cliente.setPlano()
ficha_cliente.setSaude()