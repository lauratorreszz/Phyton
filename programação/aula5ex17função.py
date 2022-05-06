def somaImposto(taxaImposto, custo):
    custo = custo +(custo*taxaImposto/100)
    return custo 

taxa = float(input('Informe o valor da taxa de imposto: '))
custo = float(input('Informe o custo do produto: '))

#custo recebe a soma e retorna a taxa e o custo 
custo = somaImposto(taxa, custo)

print('O preço com o imposto é %.2f' % custo )