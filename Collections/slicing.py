#Este concepto te permite acceder y manipular partes específicas de una secuencia (string, lista o tupla, pero en éste último NO puede crear 
#modificaciones) mediante el uso de índices.

frase = 'Supera el dolor, rendirse duele más.'
print(frase[:]) #Devuelve todo el string.
print(frase[13]) #Puedo acceder a cualquier caracter de un string de esta manera.
print(frase[13:18]) #Devuelve una parte del string.
print(frase[20:]) #Devuelve una parte del string, a partir del primer índice.
print(frase[:18]) #Devuelve una parte del string, hasta el segundo índice.
print(frase[::3]) #Devuelve una parte del string, saltando dependiendo la cantidad al índice
print(frase[::-1]) #Devuelve una parte del string, escrito al revés.

#En los conjuntos NO se puede hacer directamente porque éstos no tienen orden. Pero, puedes convertir el conjunto en una lista, hacer el slicing, y 
#luego convertirlo de nuevo. 
#Convertir listas en conjuntos ayuda a eliminar duplicados, lo cual es útil para ciertos problemas.

conjunto = {10, 20, 30, 40}
lista = list(conjunto) 
sublista = lista[1:3]
nuevo_conjunto = set(sublista)
print(nuevo_conjunto)