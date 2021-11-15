'''
Ejercicio 2.  crear un programa que pida 3 numeros y determina cual es el mayor
'''

n1= int(input("Ingrese primer  numero: "))
n2= int(input("Ingrese segundo numero: "))
n3= int(input("Ingrese tercer  numero: "))

#para ello le decimos que compare. 
#si n1 es mayo o igual(>=) que n2 y si n1 es mayor o igual que n3
if n1>=n2 and n1>=n3:
    #que nos imprima que el numero mayor es n1 como lo indicamos
    print(f"El numero mayor es: {n1}")

 
#pero si n2 es mayo o igual(>=) que n1 y si n2 es mayor o igual que n3
elif n2>=n1 and n2>=n3:
    #que nos imprima que el numero mayor es n2 como lo indicamos
    print(f"El numero mayor es: {n2}")

#pero si n3 es mayo o igual(>=) que n1 y si n3 es mayor o igual que n2
elif n3>=n1 and n3>=n2:
     #que nos imprima que el numero mayor es n3 como lo indicamos
    print(f"El numero mayor es: {n3}")