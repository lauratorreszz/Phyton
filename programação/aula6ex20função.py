import datetime


_data2.day = int(input('Digite o dia: ')) 
_data2.month = int(input('Digite o mês: '))
_data2.year = int(input('Digite o ano: '))

_data2=datetime.datetime.strptime(_data2.day,_data2.month,_data2.year, "%d/%m/%Y")
print(_data2)

print("{}/{}/{}".format(_data2.day,_data2.month,_data2.year))