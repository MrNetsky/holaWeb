#Son más ligeras, por lo que es preferente utilizarlas por encima de ls listas, ya que así podremos ahorrar memoria.
x=(1,2.75,'Hola',False,[12,45,99])
#El constructor de la tupla, es la coma, NO el paréntesis, pero el intérprete muestra los paréntesis y nosotros debieramos utilizarlos por claridad.
y=12, 
print(type(x),type(y)) 

#Los métodos y funciones que aplican para listas, también lo hacen para las tuplas, ya que son iterables, a excepción de los que modifican la lista,
#aquí devolveran un error al ser, las tuplas, inmutables.

tupla = (1, 2, 3, 2)
#Cuenta cuántas veces aparece un valor en la tupla.
print(tupla.count(2))  # Resultado: 2
#Devuelve el índice de la primera aparición de un valor.
print(tupla.index(2))  # Resultado: 1

#Son inmutables, pero como uno de los elementos de esta tupla es una lista, dicha lista SI es mutable y por ello es factible lo 
#siguiente:
my_list = ['Marull']
my_tuple = (11, 5, 1997, 1.72, 'Pablo Leandro', 'Acosta Cuestas', my_list)
my_list [0] = 'José de la Quintana'
print(my_tuple)