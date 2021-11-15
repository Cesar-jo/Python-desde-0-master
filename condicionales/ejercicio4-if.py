'''
Ejercicio 4. Cajero automatico
'''

#creamos una variable para indicar el saldo acual que tenemos para despues incrementarlo o quitarle dinero
saldo = 2000

'''
creamos un menu de 4 opciones
'''
print("1. Ingreso de dinero")
print("2. Retiro de dinero ")
print("3. Mostrar dinero")
print("4. Salir")

#creamos una varaible llamada opcion para escojer la opcion del menu que deceemos
#utilizaremos las entradas de datos con el input
opcion = int(input("Elija una opción: "))

# le deccimo si el usuario eligio en la variable opcion la opcion 1
if opcion ==1:
    #oues con la variable ingreso le decimos que con el input osea el dato de entrada
    #que ingrese el dinero que desea ingresar
     ingreso = float(input("Dinero a ingresar: "))
     #para ello se  sumara ese ingreso que puso el usuario en la variable usuario con el saldo actual
     saldo += ingreso
     #y se nos imprimira el saldo ya actualizado con la sumatoria del ingreso con el saldo actual
     print(f"Nuevo saldo en la cuenta: {saldo}")

elif opcion ==2:
    salida = float(input("Dinero de salida: "))
    #le decimos que si el saldo que quiere sacar es mayor al saldo que tiene
    if salida>saldo:
        #entonces que le imprima un mensaje de saldo insuficiente
        print("Saldo insuficiente")
        #si el saldo no es mayor al saldo actual
    else:
        #entonces restara el saldo con lo que quiere sacar de dinero osea la salida saldo actual - salida
        saldo -= salida
        print(f"Nuevo saldo disponible {saldo}")


elif opcion == 3:
    #aqui nos imprimira el saldo actual que tenemos
    print(f"Saldo disponible {saldo}")

elif opcion == 4:
    print("fin")

else:
    print("Error en la entrada de datos")
