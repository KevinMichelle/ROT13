import sys

if len(sys.argv) > 2:
	if sys.argv[1] == 'file':
		file = open(sys.argv[2], 'r')
		mensaje = file.read()
		file.close()

else:
	mensaje = sys.argv[1]

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = len(abecedario)

def cifrar(mensaje):
	cipher = ''
	for letra in mensaje:
		decision = True
		for abc in abecedario:
			if (letra == abc) or (letra.lower() == abc):
				if letra.isupper():
					indice = (abecedario.index(letra.lower()) + n/2)%n
					cipher = cipher + abecedario[indice].upper()
				else:
					indice = (abecedario.index(letra) + n/2)%n
					cipher = cipher + abecedario[indice]
				decision = False
		if(decision):
			cipher = cipher + letra
	return cipher

ciphertext = cifrar(mensaje)
print 'Ciphertext'
print
print ciphertext
print
plaintext = cifrar(ciphertext)
print 'Plaintext'
print
print plaintext
