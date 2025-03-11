#Representan colecciones de elementos únicos, lo que garantiza que cada elemento aparezca una sola vez.

#No permite integrar tipos de datos modificables (como listas o diccionarios), pero si tuplas.

conjunto = set(['dato1', 'dato2']) 
print(conjunto)
print(type(conjunto))

conjunto = frozenset(['dato1', 'dato2']) #De esta manera podemos incluir un conjunto dentro de otro
conjunto2 = {conjunto, 'dato3'}
print(conjunto2)

#Ambas son colecciones de elementos únicos. Conjuntos son mutables; se puede añadir o quitar elementos. Frozensets son inmutables; no se pueden 
#modificar después de su creación. Pero estructuralmente son lo mismo.

A = {1, 2, 3}
B = {3, 4, 5}
union = A.union(B)
print(union)  # Resultado: {1, 2, 3, 4, 5}
interseccion = A.intersection(B)
print(interseccion)  # Resultado: {3}

diferencia = A.difference(B)
print(diferencia)  # Resultado: {1, 2} (elementos en A, pero no en B)
dif_simetrica = A.symmetric_difference(B)
print(dif_simetrica)  # Resultado: {1, 2, 4, 5} (elementos únicos en cada conjunto)

A.add(4)
print(A)  # Resultado: {1, 2, 3, 4}
A.remove(4)
print(A)  # Resultado: {1, 3}

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#Dos maneras de constatar si un conjunto es un subconjunto de otro.
resultado = conjunto4 <= conjunto3
print(resultado)
print(conjunto4.issubset(conjunto3))

#Dos maneras de constatar si un conjunto es un superconjunto de otro.
resultado = conjunto3 > conjunto4
print(resultado)
print(conjunto3.issuperset(conjunto4))

conjunto5 = {1,3,5,7,9}
conjunto6 = {2,4,6,8,10}
print(conjunto5.isdisjoint(conjunto6)) #Compara si existe una coincidencia, es caso de que la haya, por más que sea solo una arrojará False.