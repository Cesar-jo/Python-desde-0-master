import math

'''
    Vamos a crear un bucle while utilizando raices cuadradas
    Para ello importamos la libreria math
    '''

num= int(input("Escriba un numero: "))
    #le decimos que mientras que num sea menor a 0, osea numeros negativos = -1 -2 -3 etc
while num<0:
        #que nos imprima que ingresemos un numero positivo
        #se va a repetir y repetir nuestro bucle hasta que escribamos un numero positivo
    print("Por favor ingrese un numero positivo")     
    num= int(input("Vuelva a ingresar un numero positivo: "))
        #imprimimos el resultado trayendo la libreria de math.sqrt y nuestra variable num
        #para saver el numero que ingreso el usuari
        #esta libreria lo que hace es sacar la rais cuadrada de un numero
        #agregamos :.2f para que solo nos muestro 2 decimales despues del . del resultado
print(f"El resultado de la raiz cuadrada es: {math.sqrt(num):.2f}")