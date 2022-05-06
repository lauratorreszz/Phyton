numeros = []
for i in range(0,4):
    numeros.append(int(input('Informe um número inteiro')))
soma = 0 
multiplicacao = 1 
for i in numeros:
    soma+= 1 
    multiplicacao += 1
print(numeros)
print('A soma dos números são %d'% soma )
print('A multiplicação dos números é %d' % multiplicacao)