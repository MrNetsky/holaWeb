"""Simples: Es necesario recordar que al ser un lenguaje de tipado 
dinámico, NO es necesario hacer esto c/vez que introducimos un dato,
esto se hace para cambiar el tipo de dato según necesitemos."""

#Enteros
a = int(1) 
#1

#Reales (c/decimales)
b = float(1) 
#1.0

#Booleano (Si o no, 0 ó 1, True or False)
c = bool(1) 
#True

#String
d = str(1) 
#'1'

'''Este parámetro me permite seguir en la misma línea y definir incluso
con qué caracter debo finalizar este print. #PD: SIEMPRE VA AL FINAL 
DEL PRINT.'''
print(a,type(a), b,type(b), c,type(c), d,type(d),end=' ')

"""Asignación múltiple:"""

día, mes, año = 11, 5, 1997 


'''Es una función que devuelve el carácter (una cadena) correspondiente
al valor ASCII especificado. 
PD: Recuerda que el valor pasado debe estar dentro del rango válido de 
valores ASCII (0-127 para ASCII estándar).
PD2: Del 0 al 32 no imprimirá valor alguno, ya que son caracteres de 
control son caracteres especiales no imprimibles que se utilizan para 
controlar dispositivos de hardware (como impresoras y terminales) o 
para proporcionar instrucciones de control en flujos de datos. En el 
código ASCII estándar, hay 33 caracteres de control en total, que van 
desde el valor 0 hasta el 31, más el carácter 127.'''

numero = 97
caracter = chr(numero)
print(caracter)  # Esto imprimirá 'a'

#De manera opuesta ord() toma un carácter y devuelve su valor ASCII
caracter = 'a'
valor_ascii = ord(caracter)
print(valor_ascii)  # Esto imprimirá 97


