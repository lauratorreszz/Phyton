numeros = []
pares = []
impares = []

for i in range(0,10):
    numero = int(input('Informe um número: '))
    numeros.append(numero)
    if (numero % 2 ==0):
        pares.append(numero)
    else:
        impares.append(numero)
print(numeros)
print(pares)
print(impares)