numeros = []
#a variável i vai de 0 a 5 (0,1,2,3,4)
for i in range(0,5):
    #append adiciona itens a uma lista 
    #para remover se usa remove
    numeros.append(int(input('Entre com um número: ')))
print(numeros)


numeros2 = []
for a in range(0,5):
    numeros2.append(int(input('Entre com um número: ')))
#invertendo a ordem de inserção
numeros2.reverse()
print(numeros2)


notas = []
for b in range(0,4):
    #insere 4 notas
    notas.append(float(input('Informe uma nota: ')))
#cria a variável soma com nada dentro dela 
soma = 0.0 
print('Notas inseridas')

#o b nao foi especificado se é string, float, int etc 
for b in range(0,4):
    #%d indica que b recebe variáveis inteiras (%d = int)
    #%f indica que b recebe numeros com virgula (%f = float), está .2f para indicar duas casas decimais (casas depois da virgula)
    print('Notas %d: %.2f' % (b,notas[b]))
    soma+= notas[b]
    
print('A média final é %.2f'% (soma/4))