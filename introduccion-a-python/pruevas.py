print("[Info] Herramienta para Multiplicar, Sumar, Restar y Dividir")
print("  ||   Escrito en Python ")
print("  ||   Mi nombre es Cesar, Espero y les guste esta pequeña herramienta\n")

print(" Hola Crack")
cadena = input("¿Cual es tu nombre amiguito?: ")
print (f"Bienvenido a tu sistema de operaciones aritmeticas en Python, My amigo: {cadena}")

'''
Ahora haremos una prueva con lo ya aprendido de las entradas y salidas de datos
'''

print("[Info] Empezamos con las Multiplicaciones")
print("  ||   Ingrese los numeros que desea multiplicar, siga las instrucciones ")
print("  ||   Mi nombre es Cesar, Espero y les guste esta pequeña herramienta\n")

#para hello desarrollaremos un sistema de multiplicacion

#primero declaramos 2 variables referentas a numero 1 y numero dos
#antes del input agregamos el tipo de dato entero, ya que va haceptar solo datos numericos de tipo int
#recuerden que el input sirve para ls entradas de datos osea para recojer informacion que le demos
# y f en los print(f) sirve la salida de los datos, osea sacar los datos que ingresamos
n1 = int(input("Ingrese primer numero a multiplicar: "))
n2 = int(input("Ingrese segundo numero a multiplicar: "))
#despues creamos otra variable para asignar el tipo de operacion que haremos en este caso multiplicacion
r = n1 * n2
#por ultimo imprimimos el resutado
print(f"Su resultado es: {r}")

print("[Info] Empezamos con las Diviciones")
print("  ||   Ingrese los numeros que desea dividir, siga las instrucciones ")
print("  ||   Mi nombre es Cesar, Espero y les guste esta pequeña herramienta\n")

'''
Divicion
'''

n1 = int(input("Ingrese primer numero a Dividir: "))
n2 = int(input("Ingrese segundo numero a Dividir: "))

r = n1 / n2
print(f"Su resultado es: {r}")

print("[Info] Empezamos con las Sumas")
print("  ||   Ingrese los numeros que desee sumar, siga las instrucciones ")
print("  ||   Mi nombre es Cesar, Espero y les guste esta pequeña herramienta\n")

'''
Suma
'''
n1 = int(input("Ingrese primer numero a sumar: "))
n2 = int(input("Ingrese segundo numero a sumar: "))

r = n1 + n2
print(f"Su resultado es: {r}")

print("[Info] Empezamos con las Restas")
print("  ||   Ingrese los numeros que desee restar, siga las instrucciones ")
print("  ||   Mi nombre es Cesar, Espero y les guste esta pequeña herramienta\n")

'''
Resta
'''

n1 = int(input("Ingrese primer numero a restar: "))
n2 = int(input("Ingrese segundo numero a restar: "))

r = n1 - n2
print(f"Su resultado es: {r}")