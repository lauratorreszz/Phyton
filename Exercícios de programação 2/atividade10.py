#exercício 10 
num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))
for intervalo in range(num1, num2):
    if (num1<intervalo<num2):
        print(intervalo)
