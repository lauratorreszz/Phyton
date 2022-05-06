#from importa apenas um pedaço da biblioteca
from datetime import datetime #as laura para nomear a biblioteca  

year = int(input("Insira o ano: "))
month = int(input("Insira o mês: "))
day = int(input("Insira o dia: "))

formatedDate = datetime(year, month, day)
print(formatedDate)

#bibliotecas mais famosas 
#numpy = biblioteca de calculo 
#matplotlib = biblioteca para graficos 
#pandas = para manipulaçao de dados