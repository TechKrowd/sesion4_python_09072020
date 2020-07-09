"""
Solicitar varios numeros enteros al usuario. 
Cuando quiera detener el programa introducirá un 0.
Mostrar por cada número introducido la suma de sus dígitos.
"""
def sumar_dig(num):
	digitos = list(map(int,str(num)))
	print(digitos)
	return sum(digitos)
	
def main():
	num = -1
	while num != 0:
		num = int(input("Introduce un número: "))
		if num!=0:
			suma = sumar_dig(abs(num))
			print("La suma es {}".format(suma))

main()