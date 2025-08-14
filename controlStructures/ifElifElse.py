bandera = 1997
if bandera == 1997:
    print('Este año llegas a los 28 años.')

bandera2 = 18
if bandera2 >= 18:
    print('Eres mayor de edad.')
else:
    print('Aún eres menor, al menos en Argentina.')

'''La construcción A if C else B en Python es una forma compacta y 
poderosa de manejar expresiones condicionales, muy útil para mantener
el código limpio y legible. Es similar al operador ternario ? : en 
lenguajes como C o Java, pero Python utiliza esta sintaxis más 
explícita.'''

num = 3
var = "par" if (num % 2 == 0) else "impar"
print (var)

bandera3 = 600000
if bandera3 < 1000000:
    print('Eres pobre, lamento comunicartelo')
elif 1000000 <= bandera3 <= 1500000: #Debe expresar la condición, al 
#igual que en el if.
    print('Bienvenido a la clase media.')
else:
    print('Hola mi rey, vos si que andas bien, no como yo!')