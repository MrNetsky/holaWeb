'''Es similar a switch en otros lenguajes. Permite comparar un valor con
diferentes patrones y ejecutar el bloque de código correspondiente.'''

animal = str(input('Ingrese un animal doméstico:'))
match animal:
    case 'Perro':
        print('Es el mejor amigo del hombre, a excepción del caniche y el chihuahua.')
    case 'Gato':
        print('El gato es un animal doméstico, pero no tan genial como un perro.')
    case 'Pez':
        print('Es un animal doméstico, pero entre nosotros, ¿Todo bien en casa?. Adopta una planta mejor.')
    case 'Hamster':
        print('Pese a que son animales doméstico, perfiero los roedores lo mas lejos de mi posible.')
#El carácter _ (guión bajo) es un caso por defecto que captura todos 
#los valores que no coinciden con los anteriores, actuando como el else.
    case _:
        print('El animal NO es doméstico. No era muy dificil la consigna que te dí.')

'''Antes de la versión 3.10, al no existir esta funcionalidad, se podía
(y aún se puede), anidar if-else:'''

animal = str(input('Ingrese un animal doméstico:'))
if animal == 'Perro':
    print('Es el mejor amigo del hombre, a excepción del caniche y el chihuahua.'),
elif animal == 'Gato':
    print('El gato es un animal doméstico, pero no tan genial como un perro.')
elif animal == 'Pez':
    print('Es un animal doméstico, pero entre nosotros, ¿Todo bien en casa?. Adopta una planta mejor.')
elif animal == 'Hamsters':
    print('Pese a que son animales doméstico, perfiero los roedores lo mas lejos de mi posible.')
else:
    print('El animal NO es doméstico. No era muy dificil la consigna que te dí.')
    
#Ó emular un switch con un diccionario.
animalDomestico = {
    'Perro' : 'Perro',
    'Gato' : 'Gato',
    'Pez' : 'Pez',
    'Hamster' : 'Hamster'
    }
ingreso = str(input('Ingrese un animal doméstico, por favor: '))
if ingreso in animalDomestico:
    print('Correcto')
else:
    print('No te pedí una medalla olímpica, sino un simple animal doméstico, intentá de nuevo y hacelo bien por el amor de Dios.')
