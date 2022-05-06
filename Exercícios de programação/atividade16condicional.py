num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
num4 = int(input('Informe o quarto número: '))

if(num1 == num2) and (num1 == num3) and (num1 == num4) and (num1, num2, num3, num4 > 0):
    print('São iguais e positivos')
elif(num1 == num2) and (num1 == num3) and (num1 == num4) and (num1, num2, num3, num4 < 0):
        print('São iguais e negativos')
else: 
    if(num1>num2) and (num1>num3) and (num1>num4) and (num1>0) and (num1 % 2 == 0):
        print('O primeiro número é o maior e é positivo e par')
        if(num1>num2) and (num1>num3) and (num1>num4) and (num1<0) and (num1 % 2 != 0 ):
            print('O primeiro número é o maior e é negativo e ímpar')
    elif(num2>num3) and (num2>num4) and (num2>0):
        print('O segundo número é o maior e positivo')
        if(num2>num3) and (num2>num4) and (num2<0):
            print('O segundo número é o maior e negativo')
    elif(num3>num4) and (num3>0):
        print('O terceiro número é maior e positivo')
        if(num3>num4) and (num3<0):
            print('O terceiro número é maior e negativo')
    elif(num4>0):
        print('O quarto número é o maior e é positivo')
        if(num4<0):
            print('O quarto número é o maior e é negativo')
        
    if(num1<num2) and (num1<num3) and (num1<num4) and (num1>0):
        print('O primeiro número é o menor e positivo')
        if(num1<num2) and (num1<num3) and (num1<num4) and (num1<0):
            print('O primeiro número é o menor e negativo')
    elif(num2<num3) and (num2<num4) and (num2>0):
        print('O segundo número é o menor e positivo')
        if(num2<num3) and (num2<num4) and (num2<0):
            print('O segundo número é o menor e negativo')
    elif(num3<num4) and (num3<num4) and (num3>0):
        print('O terceiro número é o menor e positivo')
        if(num3<num4) and (num3<num4) and (num3<0):
            print('O terceiro número é o menor e negativo')
    elif(num4>0):
        print('O quarto número é o menor e positivo')
        if(num4<0):
            print('O quarto número é o menor e negativo')
            
        



