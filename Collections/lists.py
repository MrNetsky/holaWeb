a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #Concatenación.
print(c)

print(min(c)) #Mínimo de la lista. En el caso de que operemos como 
#strings los elementos se comparan alfabéticamente. Por lo tanto, el 
#resultado será el elemento que viene primero en orden alfabético.

print(max(c)) #Máximo de la lista.En el caso de que operemos como 
#strings se compara alfabéticamente, y el resultado será el elemento 
#que viene al final en orden alfabético.

print(sum(c)) #Suma de la lista. Válido para int o float.

c.append(7) #Agrega un elemento en la última posición.

c.append(int(input('Ingrese un número p/agregar a la lista:'))) #Para 
#agregar elementos a traves de la terminal.

c.extend([7, 8, 9]) #Agrega una lista dentro de una lista.

c.insert(0,0) #En la posición indicada en el 1er índice, agrega un 
#elemento indicado en el 2do índice.  
print(c)


c.pop(2) #Elimina un elemento en una posición determinada de la lista. 
#Si no se pasa un argumento, elimina el último elemento de la lista.

c.remove(5) #Elimina un elemento en la lista, identificado por su valor.

del c[9] #Elimina de derecha a izquierda el 1er elemento coincidente.

print(c.index(7)) #Busca un valor y devuelve su posición. Admite como 
#argumento adicional un índice inicial a partir de donde comenzar la 
#búsqueda.

print(c.count(3)) #Devuelve la cantidad de repeticiones de un elemento,
#cero si no lo encuentra.

c.sort(reverse=True) #Ordena los elentos en orden descendente. #PD: Si 
#NO especificamos nada en el argumento lo hace de manera ascendente.
print(c)

c.reverse() #Invierte el orden de los elementos de una lista.
print(c)
print(len(c)) #Devuelve la cantidad de elementos que posee una lista.

d = 'Uno, Dos, Tres'.split() #Separa un string y lo convierte en una 
#lista.
print(d, type(d))

e = ','.join(['Uno',' Dos', ' Tres.']) #Crea un string a partir de una 
#lista.
print(e, type(d))

f = list('Hola') #Genera una lista y toma cada letra del string como 
#elemnto.
print(f, type(d)) 

x=[1,2.75,'Hola',False,[12,45,99]]
print(x[5][2])

datos = ['Pablo Leandro', 'Acosta Cuestas']
nombre, apellido = datos #Desempaquetado, tambien es válido para 
#conjuntos.