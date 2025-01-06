#Este concepto te permite acceder y manipular partes específicas de un string mediante el uso de índices.

frase = 'Supera el dolor, rendirse duele más.'
print(frase[:]) #Devuelve todo el string.
print(frase[13]) #Puedo acceder a cualquier caracter de un string de esta manera.
print(frase[13:18]) #Devuelve una parte del string.
print(frase[20:]) #Devuelve una parte del string, a partir del primer índice.
print(frase[:18]) #Devuelve una parte del string, hasta el segundo índice.
print(frase[::3]) #Devuelve una parte del string, saltando dependiendo la cantidad al índice
print(frase[::-1]) #Devuelve una parte del string, escrito al revés.
