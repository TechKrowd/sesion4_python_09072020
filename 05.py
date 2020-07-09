"""
Implementar una función que reciba las notas de varios alumnos
junto con el num de expediente de cada uno (alfabetico).
Devolverá el expediente con la nota más alta.
Se podrán pasar las notas separadas por comas (expediente=nota)
o se podrá pasar un diccionario.
Debe funcionar en ambos casos.
"""

def pedir_notas(n=0):
	notas = dict()
	for i in range(n):
		print(f"Alumno {i+1}")
		e = input("Expediente: ")
		nota = float(input("Nota: "))
		notas[e]=nota
	return notas

def nota_max (**kwargs):
	lista = list()
	if len(kwargs)>0:
		maxima = max(kwargs.values())
		for e in kwargs.keys():
			if kwargs[e] == maxima:
				lista.append(e)
	return lista

notas = pedir_notas(3)
expedientes = nota_max(**notas)
#expedientes = nota_max(aa=5.7,bb=6.5,cc=6.5)
print(expedientes)
