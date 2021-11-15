#Ejercisio 1, haremos un ejercicio utilizando las entradas y salidas de datos
#El programara sera un resolvedor de ecuaciones

#utilizaresmos un tipo de dato float ya que el resultado de la resolucion de ecuaciones nunca son de tipo entero(int)
#y el tipo de dato float tambien nos permite ingresar datos enteros o desimales
a= float(input("Ingrese el valor de (a):"))
b= float(input("Ingrese el valor de (b):"))
c= float(input("Ingrese el valor de (c):"))

#creamos una variable para los resultados, 
# en esta variable ira la formula de la ecuacion a resolver 
# de este ejercisio

'''
la formula que utilizaremos es la siguiente

(c+5)(b²-3ac)a²            OJO: recuerden que los espacios basias despues de los ()estos espacios() cuentan
_________________                como multiplicacion, asi seia entonces: (c+5)*(b²-3ac)*a²/4
        4a                    recuerden que para elevar al cuadrado un numero o potecia es con **


'''

r= ((c+5)*(b**2-3*a*c)*a**2)/(4*a)

#Recuerden que la f despues del print es para la salida de datos que ingresamos
print(f"Su resultado es: {r}")