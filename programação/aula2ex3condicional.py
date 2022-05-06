nota1 = float(input('Informe a primeira nota'))
nota2 = float(input('Informe a segunda nota'))
media = (nota1+nota2)/2.0 
#usamos ponto para números com vírgula 
print('A média é', media)

if(media==10):
    print('Aprovado com excelência')
elif(media>=7): #elif(media>=7) and (media<=8):
    print('Aprovado')
else:
    print('Reprovado')
#o programa testa se o if é verdadeiro, depois o elif, e finalmente o else
#um = é atribuição (guarda na memória)
#dois == é igualdade
