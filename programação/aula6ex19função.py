def retornaInvertido (valor):
    #dois pontos dentro do vetor (vetor smp tá em colchetes) significa para rodar ao contrário, neste caso, invertendo o valor
    return valor [::-1]

numero = input('Informe um número')
print(retornaInvertido(numero))