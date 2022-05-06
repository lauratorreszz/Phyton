
from atividade5 import Conta 

class ContaInvestimento(Conta):
    def  __init__(self, numero, nome, saldo, taxaJuros ):
        super().__init__(numero, nome, saldo)
    
    def setTaxaJuros(self, taxaJuros):
        self.taxaJuros = taxaJuros
        
    def getTaxaJuros(self):
        return self.taxaJuros
    
    def adicioneJuros(self):
        pass 

contaInvestimento = ContaInvestimento
contaInvestimento.setTaxaJuros()
contaInvestimento.adicioneJuros()
print(contaInvestimento.adicioneJuros)
