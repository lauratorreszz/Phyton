print('Compara duas strings')

string1 = input('String 1')
string2 = input('String 2')

print('Tamanho de %s: %d caracteres') % (string1, len(string1))
print('Tamanho de %s: %d caracteres') % (string2, len(string2))

if (len(string1) != len(string2)):
    print('As duas strings são de tamanhos diferentes')
    print('As duas strings são de conteúdos diferentes')
else:
    print('As duas strings tem tamanhos iguais')
    if(string1 == string2):
       print('As duas strings tem o mesmo conteúdo')
    else:
        print('As duas strings possuem conteúdos diferentes')
    
    
    
#exemplo do yuri
user = password = ""
while user == password:
    user = str(input("Insira o nome de usuário: "))
    password = str(input("Insira a senha: "))
    if password == user:
        print("o usuário e a senha devem ser diferentes\n")
    else:
        print("log in aprovado")
    
