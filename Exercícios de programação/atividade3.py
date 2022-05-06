#exercício 3
import math 

raio = float(input('Digite o raio da circunferência'))
print('A área da circunferência é', math.floor(math.pi*(raio**2)) , 'e o perímetro é', math.floor(2*math.pi*raio))
#math.floor para arredondar para baixo e math.ceil para cima