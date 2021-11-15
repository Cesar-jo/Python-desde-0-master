'''
Ejercicio 1. Crear un programa que pida 2 numeros y obtenga
como resultado cual de ellos es par o si ambos lo son
'''

n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese segundo numero: "))

#entonces le decimos que si n1 entre / 2 = 0 y n2/2 tambien es = 0, entonces ambos son numeros pares
if n1%2==0 and n2%2==0:
    print("Ambos son pares")

#elid= pero si n1/2 = 0 y n2 /2 es diferente(!=) a, entonces solo el primer numero es par 0
elif n1%2==0 and n2%2!=0:
    print(f"{n1} es un numero par")

    # ahora hacemos lo contrario si el otro numero es par  

#elid= pero si n1/2 != 0 es diferente(!=) a 0 ,  y n2/2 == 0 entonces solo el segundo numero es par 
elif n1%2!=0 and n2%2==0:
    print(f"{n2} es un numero par")

#ahora si ninguno
else:
    print("Los dos son numeros inpares")