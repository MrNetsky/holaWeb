'''While: repite la ejecución de un bloque de código siempre que una 
expresión sea verdadera.'''

print ('¡Bienvenido al programa de multiplicaciones!')
n = int(input('Ingrese un entero:'))
m = int(input('Dime cuantas veces quieres que se multiplique:'))
c = 1
while c < m:
    print('-----',n, '*', c, '=',n * c,'-----')
    c+=1 
'''#IMPORTANTÍSIMO NO OLVIDAR EL CONTADOR, de lo contrario podriamos 
caer en un bloque infinito. Aún mas si tu equipo es de bajos recursos.
Podemos interrumpir con Ctrl + C'''

'''Es ligeramente más rápida al no depender de una variable de control
(aunque la diferencia de rendimiento sería imperceptible en este
caso).'''
while True:
    entrada = input("Escribe algo: ")
    if entrada == "adios":
        break  # Salimos del bucle si el usuario escribe "adios"
    else:
        print(entrada)  # Mostramos lo que el usuario ingresó

'''Es más explícita y puede ser preferida en situaciones donde necesitas
manejar varias condiciones de salida de manera centralizada. Proporciona
mayor flexibilidad para ampliaciones, como agregar más verificaciones en
el futuro.'''
salir = False
while not salir:
    entrada = input()
    if entrada == 'adios':
        salir = True
    else:
        print (entrada)

'''Comprueba si la edad es par, en cuyo caso saltamos a la próxima 
iteración en lugar de imprimir el mensaje.'''
edad = 0
while edad < 18:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print ('Felicidades, tienes', str(edad))
    
clave = '123abc'
intentos = 1
ingreso = str(input('Ingresa la clave por favor: '))

while ingreso != clave:
    print('Clave incorrecta.')
    intentos += 1
    ingreso = str(input('Ingresa la clave, nuevamente por favor: '))
    if intentos == 3:
        print('Acceso denegado, demasiados intentos.')
        break
else:
    print('Acceso permitido.')