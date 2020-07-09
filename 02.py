"""
Pedir por teclado dos números. 
El segundo número solo puede tener un dígito(0-9).
Comprobar cuantas veces aparece el digito en el primer número.
"""

def pedir_numeros():
	num = int(input("Introduce un número: "))
	dig = int(input("Introduce un dígito: ")[0])
	return num, dig

def contar (num=0, dig=0):
	digitos = list(map(int, str(num)))
	return digitos.count(dig)

def contar_str (num=0, dig=0):
	num_s = str(num)
	return num_s.count(str(dig))

def main():
	num, dig = pedir_numeros()
	n = contar_str(num,dig)
	print("{} aparece {} veces en {}".format(dig,n,num))

main()