import sys

filename = sys.argv[1]

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

file = open(filename, 'r')
texto = file.read()
file.close()

#print texto


conteos = []
porcentaje = []

total = 0
for letter in abc:
	conteo = 0
	for l in texto:
		if(letter == l):
			conteo += 1
	total += conteo
	conteos.append(conteo)

suma = 0

for index, elemento in enumerate(conteos):
	div = 0
	if total > 100.0:
		div = elemento*(100.0/total)
	else:
		div = (100.0/total)*elemento
	tupla = abc[index], div
	porcentaje.append(tupla)
	suma += div

tupla = sorted(porcentaje, key=lambda x: x[1], reverse=True)
file = open('frecuencia', 'w')
for i in tupla:
	line = ' '.join(str(x) for x in i)
	file.write(line + '\n')
file.close()
