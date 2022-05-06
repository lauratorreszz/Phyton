#exercicio 7 
num1, num2, num3, num4, num5 = int(input('Insira um número inteiro: ')), int(input('Insira um número inteiro: ')), int(input('Insira um número inteiro: ')), int(input('Insira um número inteiro: ')), int(input('Insira um número inteiro: '))
if (num1>num2) and (num1>num3) and (num1>num4) and (num1>num5):
    print('O primeiro número é o maior')
elif (num2>num3) and (num2>num4) and (num2>num5):
    print('O segundo número é o maior')
elif (num3>num4) and (num3>num5):
    print('O terceiro número é o maior')
elif (num4>num5):
    print('O quarto número é o maior')
else:
    print('O quinto número é o maior')