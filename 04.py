"""
Implementar una función a la que se le puedan pasar
varios números separados por comas y devuelva el mayor y el 
menor de todos ellos.
La cantidad de números podrá variar.
"""

def max_min(*args):
	maximo = max(args)
	minimo = min(args)
	return maximo, minimo

#numeros = [5,2,8,3]
#max_min(*numeros)
maximo, minimo = max_min(5,2,8,3)
print("Máximo: {}, Mínimo: {}".format(maximo, minimo))