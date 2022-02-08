# '''
# string = '012345678901234567890123456789012345678901234567890123456789'
# lista = ['0123456789','0123456789','0123456789','0123456789','0123456789','0123456789',]
# retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
# '''

# string = '012345678901234567890123456789012345678901234567890123456789'
# n1 = string[0:10]
# n2 = string[10:20]
# n3 = string[20:30]
# n4 = string[30:40]
# n5 = string[40:50]
# n6 = string[50:60]
#
# print(n1,n2,n3,n4,n5,n6)
# #lista = list(n1+n2+n3+n4+n5+n6)#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lista = list(n1 and n2 and n3 and n4 and n5 and n6)
# print(lista)

string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i:i + n] for i in range(0, len(string), n)]
raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(contadores)
#[0, 10, 20, 30, 40, 50]

print(tuplas)
#[(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60)]

print(raw)
#['string[0:10]', 'string[10:20]', 'string[20:30]', 'string[30:40]', 'string[40:50]', 'string[50:60]']

print(lista)
#['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']

print(retorno)
#0123456789.0123456789.0123456789.0123456789.0123456789.0123456789
