nota = -1
while (nota<0) or (nota>10):
    nota = int(input('Informe uma nota'))
    if (nota<0) or (nota>10):
        print('Nota inválida')
    else:
        print('Nota certa')
#enquanto eu digitar uma nota menor que 0 ou maior que 10, o sistema continuará a pedir a nota
#dentro do while a multiplicação é feita com *=, assim como toda operação matematica vai precisar de = (+=, <= etc)

#senha = 123
#while (senha != 123):
    #senha = int(input('Coloque sua senha'))
#!= é sinal de diferente 
