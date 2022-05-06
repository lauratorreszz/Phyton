#exercício 1 
nota = -1
while (nota<0) or (nota>10):
    nota = int(input('Insira uma nota entre zero e dez: '))
    if (nota<0) or (nota>10):
        print('Nota inválida')
    else:
        print('Nota válida')