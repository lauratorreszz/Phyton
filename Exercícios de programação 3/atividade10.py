class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        pass
    
    def settipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
        
    def gettipoCombustivel(self):
        return self.tipoCombustivel
    
    def setvalorLitro(self, valorLitro):
        self.valorLitro = valorLitro
        
    def getvalorLitro(self):
        return self.valorLitro 
    
    def setquantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel 
        
    def getquantidadeCombustivel(self):
        return self.quantidadeCombustivel 
    
    def abastecerPorValor(self, valorLitro):
        print(self.quantidadeCombustivel)
        
    def abastecerPorLitro(self, quantidadeCombustivel):
        print(self.valorLitro)
    
    def alterarValor(self, valorLitro):
        pass
    
    def alterarCombustivel(self, tipoCombustivel):
        pass
    
    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        pass
    
bomba = bombaCombustivel
bomba.setquantidadeCombustivel()
bomba.settipoCombustivel()
bomba.setvalorLitro()
bomba.alterarCombustivel()
bomba.alterarQuantidadeCombustivel()
bomba.alterarValor()
bomba.abastecerPorLitro()
bomba.abastecerPorValor()