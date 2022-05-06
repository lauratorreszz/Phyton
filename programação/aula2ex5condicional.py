valor = float(input("Informe um número:"))


print("1 - Par ou ímpar?")
print("2 - Positivo ou negativo?")
print("3 - Inteiro ou decimal?")

opcao = input("Escolha uma opção")

if(opcao == "1"):
    if(valor % 2 == 0):
        print("Valor é par")
    else:
        print("Valor é ímpar")
elif (opcao == "2"):
    if(valor <0):
        print("Negativo")
    else:
        print("Positivo")
elif (opcao == "3"):
    if(valor == float(valor)):
        print("Decimal")
    else:
        print("Inteiro")
else: 
    print('Valor inválido')
#uma porcentagem pega o resto da divisão por 2 
#duas porcentagens é porcentagem 