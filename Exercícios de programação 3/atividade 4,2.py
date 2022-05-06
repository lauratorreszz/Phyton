class Pessoa():
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos):
        self.idade += anos
        if (self.idade < 21):self.crescer(0.5)
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
    def crescer(self, altura):
        self.altura += altura
        
a = Pessoa("Yuri", 19, 68, 156)

a.engordar(6-3)
a.emagrecer(18)
a.crescer(2)
a.envelhecer(1)
print(vars(a))
