#Como clave podemos usar cualquier valor inmutable.
#NO son secuencias, pese a que son iterables, es un mapeado.
a ={
    'nombre' : 'Pablo Leandro',
    'apellido' : 'Acosta Cuestas',
    'año' : 199
}

print(a.keys()) #Devuelve las claves, tambien sirve para iterar.
print(a.get('año')) #Devuelve el valor de una clave
#Es útil buscar por este método ya que buscando de otra manera, si no encuetra lo que busca, generará un error. Mientras que aquí, simplemente 
#devolverá un 'none', indicando que NO encontró el valor buscado (Pero el programa continuará).
print(a.values())
print(a.items()) #Devuelve un objeto con pares clave-valor como tuplas.
a.update({'año': 1997, 'día' : 11})

del a ['año'] #Elimina un elemento.
a.pop('año') #En el segundo caso, podrías usar el valor después.
print(a)
a.clear() #Elimina TODOS los elementos.
print(a)

#Para un diccionario ad hoc, la sintaxis {clave: valor} es más rápida y clara. Pero si necesitas un diccionario vacío o crear uno a partir de una 
#secuencia de pares, dict() es útil.
#Las tuplas y los conjutos, pueden ser claves. Las listas NO.

conjunto = {1, 2, 3}
diccionario = {clave: clave ** 2 for clave in conjunto}
print(diccionario)

conjunto = {1, 2, 3}
dicccionario = {frozenset([x]): x for x in conjunto}
print(diccionario)

p = dict.fromkeys(['x', 'y']) #Crea diccionarios con datos sin definir.
print(p)
q = dict.fromkeys(['x', 'y'], 'No se') #Cambiando el valor por defecto.
print(q)
conjunto = {1, 2, 3}
diccionario = dict.fromkeys(conjunto, 'valor')
print(diccionario)
r = dict.fromkeys('ABCDE', 'Hola') #El primero objeto es iterable y utilizará a cada caracter que contenga como clave, mientras el 2do
#será el valor que contenga c/u de esas claves.
print(r)