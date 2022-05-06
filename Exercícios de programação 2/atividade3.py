nome=str(input("bota o nome ai: "))
while ( len(nome) <=  3 ):
	nome=str(input("bota o nome ai: "))

idade=int(input("bota a sua idade ai: "))
while ( idade > 150 or idade < 0 ):
	idade=int(input(("bota sua idade ai: ")))

salario=float(input("bota seu salario ai: "))
while ( salario < 0 ):
	salario=float(input("bota seu salario ai: "))

sexo=str(input("macho ou femea: "))
while  sexo !="f" and sexo!="m" :
	sexo=str(input("macho ou femea: "))