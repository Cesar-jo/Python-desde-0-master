'''
Ejercicio numero 2
'''

#Crear un algoritmo que intercanbie valores o variables en este caso

#primero creamos dos variables, utilizaremso las entradas de datos y salidas con los inpyt y las f en los print

a= input("(a) es igual a:")
b= input("(b) es igual a:")

#ahora vamos  intercambiar los valores que ingresamos y lo hacemos de la siguiente forma
#para ello escribimos las variables que tenemos a segido de una coma b  a,b
#a,b que sera igual ahora si invertimos los datos, para que ahora b sea igual a (a)
#y quedaria asi a,b = b,a
a,b = b,a

print(f"El nuevo valor de a es: {a} \nEl nuevo valor de b es: {b}")
  