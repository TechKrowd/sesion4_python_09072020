"""
Pedir una lista de temperaturas por teclado.
Obtener dos nuevas listas a partir de la primera.
Una contendrá los valores positivos y otra los negativos
"""

def pedir_datos(n=0):
	lista = list()
	for i in range(1, n+1):
		n = float(input(f"Introduce la temperatura {i}: "))
		lista.append(n)
	return lista

def separar_temps(temps):
	pos = list()
	neg = list()

	for t in temps:
		if t<0:
			neg.append(t)	
		elif t>0:
			pos.append(t)
	return pos, neg

def main():
	n = int(input("Introduce número de temperaturas: "))
	temps = pedir_datos(n)
	
	temps_pos, temps_neg = separar_temps(temps)
	print(temps)
	print(temps_pos)
	print(temps_neg)

main()