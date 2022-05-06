alunos = []
#5 pessoas cadastradas
for i in range(0,5):
    alunos.append(input('Informe sua idade'))
    alunos.append(input('Informe a sua altura'))
    
#segundo for, para buscar dentro de alunos a informação que eu quero
for x in alunos:
    #pega informações do primeiro e segundo alunos cadastrados
    #%s - variável caracter
    #no for, obrigatoriamente precisamos fazer apontagem 
    print('Idade: %s - Altura: %s' % (alunos[0], (alunos[1]))
    #print('Idade: %s - Altura: %s' % (alunos[0]))
    #print('Idade: %s - Altura: %s' % (alunos[1]))