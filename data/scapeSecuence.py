"""Sirven para introducir en el interior de una cadena de caracteres 
algunos caracteres especiales imposibles de representar mediante texto.
"""

print('Hola \nPablo') #Salto de linea

print('Hola \tPablo') #Tab horizontal

print('Hola \vPablo') #Tab vertical (puede variar según el terminal)

print('Hola \\Pablo') #Barra invertida

print('Hola \'Pablo\'') #Comillas simples

print('Hola \"Pablo\"') #Comillas dobles

print ('Hola\000 Pablo') #Caráter nulo, puede NO tener un efecto visual

print ('Hola\r Pablo') #Ignora lo escrito antes de la seciencia de 
#escape

print ('Hola\f Pablo') #Salto de página o avance de formulario (puede 
#variar según el terminal)

print ('Hola\a Pablo') #Carácter de alerta (hace un sonido, si está 
#habilitado).

print ('Hola \bPablo') #Elimina el caracter anterior


print(r'Hola \nPablo') #Raw string: Ignora todas las secuencias de 
#escape

print(repr('Hola \nPablo')) #Representación oficial de la cadena, 
#muestra #las secuencias de escape (Otra manera de ignorar las 
#secuencias de escape)

#Escribir las que faltan, ver el copilot!