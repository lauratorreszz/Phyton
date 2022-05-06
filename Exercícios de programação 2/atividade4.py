populacaoA = float(80000)
TaxaA = float(3/100)

populacaoB = float(200000)
TaxaB = float(TaxaA/2)

anos = int(0)

while populacaoA < populacaoB:
    anos+=1
    populacaoA+= populacaoA*TaxaA
    populacaoB+= populacaoB*TaxaB

print("\nEm ",anos,"anos, a população a será maior que a B.")