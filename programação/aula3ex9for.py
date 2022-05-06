letras = []
vogais = ['A', 'E', 'I', 'O', 'U']
for i in range(0,5):
    #converte todas as letras em maisculo 
    letras.append(input('Insira um caracter: ').upper())
    
toConsoantes = 0 
consoantes = []

for i in range(0,10):
    #se as letras q eu digitar não tiver as vogais
    if letras[i] not in vogais:
        consoantes.append(letras[i])
        toConsoantes += 1
print('Você digitou %d consoantes' % toConsoantes)
print(consoantes)
