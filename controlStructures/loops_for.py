'''For: repite la ejecución de un bloque de código, sino tantas veces 
como elementos contenga una secuencia o colección a recorrer.'''

lenguaje = 'Python'
for letra in lenguaje:
    print(f'* {letra} *')
    
'''Al igual que el bucle while, el bucle for admite las sentencias 
continue, break y else pero no es tan común su utilización.

range(): Suele usarse en conjunto con for.
Puede recibir hasta tres parámetros, siempre números enteros (int) y
debe recibir al menos uno para su ejecución. Si recibe un sólo número 
entero como argumento, comenzará desde el 0, se incrementará de a una 
unidad y se detendrá antes del número especificado;'''
for valor in range(7):
    print(valor, end= "  //  ")
'''Si recibe dos parámetros, el primero indicará el comienzo de la 
secuencia, se incrementará de a una unidad y se detendrá antes del 
segundo;'''
for valor in range(1, 7):
    print(valor, end= "  //  ")    
'''Si recibe tres parámetros, el primero será el comienzo, el segundo
será el final (siempre quedando excluido) y el tercero indicará como se
incrementarán (o decrementarán) los valores (paso).'''
for valor in range(1, 7, 2): 
    print(valor, end= "  //  ") 
'''el salto, debe ser de tipo int, por lo que float generará un error. 
Pero el salto SI puede ser negativo y recorrerá el string al reves.'''