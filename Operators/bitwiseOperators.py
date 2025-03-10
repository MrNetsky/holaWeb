#Realizan comparaciones bit a bit de dos números (de tipo int, byte, short y long), generando un nuevo número binario, que se traduce en el 
#resultado al tipo de dato ingresado origenalmente.

x= 3&2 #Devolverá 1 si y solo si ambos numeros poseen un 1 en determinada posición, de lo conrario devolverá 0.
print(x, type(x)) #Por ello da como resultado (10 = 2).

y= 3|2 #Devolverá al menos uno de los numeros poseen un 1 en determinada posición, de lo conrario devolverá 0.
print(y, type(y)) #Por ello da como resultado (11 = 3).

z= 3^2 #Coloca un 1 en la posición del bit si uno y solo uno de los bits en esa posición es 1.
print(z, type(z)) #Por ello da como resultado (01 = 1).

w= ~3 #El operador NOT invierte los bits y cambia el signo.
print(w, type(w)) #Por ello da como resultado (011 ==> 100 = -4).

p= 37>>2 #Elimina tantos dígitos desde derecha a izquierda como indique el desplazamento.
print(p, type(p)) #100101 ==> 1001 = 9.

q = 5<<3 #Agrega tantos 0 como indique el desplazamiento.
print(q, type(q)) #101 ==> 101000 = 40.