a = 4
b = 7

if a & b > 5: #AND: Validará la opción si y solo si ambos cumplen la condición
    print('Soy el verdadero.')
else:
    print('Soy el falso.')

if a | b > 5: #OR: Validará la opción si alguno cumple la condición
    print('Soy el verdadero.')
else:
    print('Soy el falso.')
    
if not a | b > 5: #NOT: Devolverá como resultado, lo opuesto (True --> False ó False -->True)
    print('Soy el verdadero.')
else:
    print('Soy el falso.')