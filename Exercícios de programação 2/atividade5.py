populacaoA = int(input("\nInsira a quantidade de habitantes da menor população\n"))
TaxaA = float(input("\nInsira a taxa de crescimento dessa população\n"))

populacaoB = int(input("\nInsira a quantidade de habitantes da maior população\n"))
TaxaB = float(input("\nInsira a taxa de crescimento dessa população\n"))

anos = int(0)

while populacaoA < populacaoB:
    anos+=1
    populacaoA+= populacaoA*(TaxaA/100)
    populacaoB+= populacaoB*(TaxaB/100)

print("\nEm ",anos,"anos, a menor população será a maior.")