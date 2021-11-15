'''
Entrada de datos
'''

#emprezamos con una imprecion de cadenas
#para pedir datos al usuario se utiliza el input

#utilizamos el input para la entrada de datos osea lo que queremos ingresar despues del : que agregemos
cadena = input("¿Como se llama tu proyecto?: ")

'''
para poder imprimir datos numericos en la salida de datos
devemos especificar que tipo de dato es el que se esta ingresando en la etrada de datos del "inpit"
ya sea enteros(int) booleanos (bool), Flotante (float), etc

para usar el tipo de dato texto o string no hace falta convertirlo
 como ya vimos en el ejemplo de la variable cadena = input("¿Como se llama tu proyecto?: ")
'''
numero = int(input("Y ¿Cual es la version de tu proyecto?: "))


#y para imprimir la salida de datos utilisamos la letra f para indicar que es una imprecion con salida de datos
#y llamamos a nuestra variable cadena con los corchetes{cadena} para imprimir los datos ingresados en esa variable
#para que por ultimo salgan impresa la salida de datos
print(f"Tu proyecto se llama: {cadena} y La version de tu proyecto es la: {numero}")


