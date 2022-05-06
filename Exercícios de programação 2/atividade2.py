#exercício 2 
nome = input('Insira seu nome de usuário: ')
senha = input('Insira sua senha: ')
while (nome == senha):
    print('Senha inválida')
    senha = input('Insira uma senha válida: ')
print('Senha válida')