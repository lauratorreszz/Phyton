import math 

#exercício 1 
base = float(input('Digite a base do triângulo '))
altura = float(input('Digite a altura do triângulo '))
print('A área do retângulo é', base*altura, 'e o perímetro é', (base*2)+(altura*2))

#exercício 2 
lado = float(input('Dê a medida de um lado do quadrado'))
print('A área do quadrado é', lado*lado, 'e o perímetro é', lado*4) 

#exercício 3 
raio = float(input('Digite o raio da circunferência'))
print('A área da circunferência é', math.floor(math.pi*(raio**2)) , 'e o perímetro é', math.floor(2*math.pi*raio))
#math.floor para arredondar para baixo e math.ceil para cima

#exercício 4 
lado1 = float(input('Digite um lado do triângulo '))
lado2 = float(input('Digite um lado do triângulo '))
lado3 = float(input('Digite um lado do triângulo '))
print('O perímetro do triângulo é', lado1+lado2+lado3)

