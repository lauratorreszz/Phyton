def verificaPositivo(valor):
    #neste caso, o 'valor' é uma variável LOCAL, OU SEJA, só funciona dentro do def
    if(valor>0):
        return 'Positivo'
    else:
        return 'Negativo'

#as variaveis fora do def são as variaveis GLOBAIS
numero = int(input('Informe um número: '))
print('O número é %s' % verificaPositivo(numero))  


