#os vetores guardam nada pois o usuário falará oq irá guardar
vetor1 = []
vetor2= []
vetor3 = []

input('Informe os valores do primeiro vetor')

for i in range(0,5):
    vetor1.append(int(input('Informe um número')))
    
for i in range(0,5):
    vetor2.append(int(input('Informe um número')))

for i in range(0,5):
    #pego oq tá armazenado em vetor 1 e vetor 2 e mostro 5 vezes na posiçao de memoria do vetor 3 
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(vetor3)