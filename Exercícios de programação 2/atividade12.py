#exercício 12 
numero = int(input('Insira o número inteiro que deseja ver a tabuada: '))
print('-'*12)
for tabuada in range(1, 11):
    print('{} x {} = {}'.format(numero, tabuada, numero*tabuada))
print('-'*12)