num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número: '))
num3 = int(input('Informe um número: '))

if(num1 == num2) and (num1 == num3):
    print('São iguais')
else: 
    if(num1 > num2) and (num1 > num3):
        print('O primeiro número é o maior')
    elif(num2 > num3):
        print('O segundo número é o maior')
    else:
        print('O terceiro número é maior')
        
    if(num1<num2) and (num1<num3):
        print('O primeiro número é o menor')
    elif(num2 < num3):
        print('O segundo número é o menor')
    else:
        print('O terceiro número é o menor')
#if dentro de outro if