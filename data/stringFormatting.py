'''IMPORTANTÍSIMO: UN MÉTODO ES UNA FUNCIÓN APLICADA A UN OBJETO.'''
"""El formateo de cadenas te permite controlar cómo se muestran los 
datos en tus programas, haciendo que el código sea más legible y 
mantenible."""

nombre = "Pablo Leandro"
profesion = "Despachante en JCMelano"
nacimiento = "11/05/1997"

'''Concatenación: Usas comas para combinar texto y variables (También
#podemos usar '+' para concatenar, pero es menos legible y no se 
recomienda).'''

print('Hola, mi nombre es', nombre, 'nací el', nacimiento, 'y soy', profesion)

'''.format: Es un método para insertar variables en posiciones 
específicas dentro de una cadena de texto. En caso de que no se 
especifique posción alguna, se imprimirán en el orden en el que se 
ingresaron dentro del .format'''
print('Hola, mi nombre es {}, nací el {} y soy {}'.format(nombre, nacimiento, profesion))

'''F-strings: Usas una f antes de las comillas para insertar variables 
directamente dentro de la cadena de texto. es a menudo preferido por 
ser más conciso y fácil de leer, especialmente cuando tienes muchas 
variables para insertar en la cadena. Es importante el uso de la 'f' 
antes de las comillas, porque de lo contrario, las llaves pierden su 
funcionalidad y pasan a escribirse, como parte del string.'''

print(f'Hola, mi nombre es {nombre}, nací el {nacimiento} y soy {profesion}') 

"""Formateo c/especificaciones"""

x = 0.123456789
y = 3.141592654
z = 11
print(f'Cortar el valor en 4 decimales: {x: .4f}')
print(f'Imprimir el valor como porcetaje: {x: .4%}')
print(f'Formato exponencial: {x: e}')
print(f'Escribir el número como binario: {z: b}') #P/Enteros
print(f'Escribir el tipo de dato {y: f}') #Error si NO se escribe el 
#tipo CORRECTO de la variable.
print(f'Escriba el valor de z-y: {z-y}')

"""Modificadores de cadena"""
a = 'hola Pablo'
b = 'CÓMO ESTAS?'
c = '1594'
d = 'Genio del mal del 1997'

print(dir(a)) #Devuelve la lista de atributos válidos del objeto.

print(a.upper()) #Mayúsculas.
print(b.lower()) #Minúsculas.
print(a.capitalize()) #Todo minúscula, menos la 1ra letra.

print(b.find('S')) #Encuentra lo que pidas siguiendo el orden de una lista. 
'''PD1: Si el valor buscado NO existe, arrojará -1. 
PD2: Si buscas una palabra arrojará el valor numérico de la posción en
donde comienza.
PD3: Si buscas una letra, arrojará el valor de la posición de la 1ra 
vez que la encuentre.'''
print(b.index('S')) #Igual que la anterior, pero si no encuentra lo que 
#buscamos, arrojará una excepción.

print(c.isnumeric()) #T or F, dependiendo de si es un valor numérico
print(c.isalpha())  #Verifica si todos los caracteres son letras. 
#IMPORTANTE: los caracteres especiales, NO cuentan (Por ej: espacio)
print(d.isalnum())  #Verifica si todos los caracteres son valores 
#alfanuméricos. IMPORTANTE: los caracteres especiales, NO cuentan 
#(Por ej: espacio)

print(a.count('z')) #Numera la cantidad de veces que encuentra una 
#coincidencia.
print(len(b)) #Numera la cantidad de caracteres de un string

print(a.startswith('h')) #Verifica cómo empieza una cadena.
print(b.endswith('?')) #Verifica cómo termina una cadena.

print(a.replace('h', 'H')) #Cambia determindado sector de un string, 
#por otro. Si no encuentra coincidencia, devuelve la cadena sin 
#modificar.

e =d.split(' ') #Separa los elementos, creando una lista.
print(e[0])
print(type(e))

f = 'Codo a Codo'
print(f.replace('Codo', 'Mano')) #Reemplaza lo escrito en el 1er índice 
#por lo que está escrito en el 2do índice. Es importante destacar que 
#hay distinción entre mayúsculas y minúsculas.
print('-'.join(f)) #Separa cada caracter por lo escrito entre entre las 
#comillas.

print(f.find('Codo')) #Devuelve la posición donde encuentra str en la 
#cadena. Si no lo encuentra devuelve -1. Se puede indicar los subíndices
#desde (inicio) y hasta (fin) donde buscar.
print(f.rfind('Codo')) #Es similar a find, pero busca la última 
#aparición.

g = '---Codo-a-Codo----'
print(g.rstrip('-')) #Devuelven cadenas a las que se les han quitado 
#los caracteres indicados, a la derecha.
print(g.lstrip('-')) #Devuelven cadenas a las que se les han quitado 
#los caracteres indicados, a la izquierda.
print(g.strip('-')) #Devuelven cadenas a las que se les han quitado 
#los caracteres indicados, al inicio y al final de la cadena.


