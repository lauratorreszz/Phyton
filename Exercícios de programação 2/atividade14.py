#exercício 14 

pares = 0
impares = 0

for i in range(0,10):
    numero = int(input('Informe um número inteiro: '))
    if (numero % 2 ==0):
        pares = pares + 1 
    else:
        impares = impares + 1 
print('A quantidade de números pares é:', pares)
print('A quantidade de números ímpares é:', impares)