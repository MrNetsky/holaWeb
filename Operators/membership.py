#El operador “is” es un operador de identidad, devuelve true cuando dos variables apuntan al mismo contenido de memoria.
nombre = "Pablo Leandro"
profesion = "Despachante en JCMelano"

nombre is profesion #False

#El operador “in” es un operador de pertenencia, compara conjuntos de elementos y devuelve true si el primero es subconjunto del segundo. 
a = [1,2,3,4,5,6,7,8,9]
b = 7

b in a #True
b not in a #False