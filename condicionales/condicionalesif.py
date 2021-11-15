'''
Condicionales if, ifelse, else
'''

#creamos una variable llamada dato
#utilizamos las entradas de datos con el input
dato = int(input("Ingrese un numero: "))
#empezamos. le decimos que si escribimos en nuestra variable dato un numero mayor que 0
if dato>0:
    #que nos imprima que el numero es positivo
   print("El numero es positivo")

#el elif = pero si. pero si el dato que escribimos es = a 0, por ende es 0, y que nos lo imprima
elif dato == 0:
    print("Resultado 0")

# el else sirve como negacion, osea funciona asi:
#si no es mayor a cero o no es igual a 0
#entonces es un numero negativo,
#y lo imprimimos
else:
    print("El numero es negativo")

print("Fin...")