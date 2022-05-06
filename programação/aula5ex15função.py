#funções separam as funcionalidades do meu sistema, para que seja mais organizado
#pode haver variáveis q só existem dentro de uma função

#coloque um nome coerente com o que vai acontecer
#os parâmetros são as coisas dentro dos parênteses, nesse caso os valores
def soma (valor1, valor2, valor3):
    return valor1 + valor2 + valor3
#AS FUNÇÕES SEMPRE VEM ACIMA DO CÓDIGO PRINCIPAL

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

#preciso fazer um apontamento pois está armazenado na memoria 
print('A soma final é: %d' % soma(valor1, valor2, valor3))