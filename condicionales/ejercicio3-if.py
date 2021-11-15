'''
Ejercicio 3. Crear un programa que compare dos nombres, y verificar si hay coincidencia o no,
si es que ambos nombres comienzan con la misma letra o si terminan con la misma letra.
'''

#utilizamos el metodo input para la entrada de datos y print(f) para la salida

nombre1= input("Nombre 1: ")
nombre2= input("Nombre 2: ")

#la condicional

#Si el nombre 1 coincide con el nombre 2, pero solo vamos a ver si coinciden las primera letra o con la ultima
#para ello utilizamos los indices que se habren con los corchetes[]
#adentro de esos corchetes[] ira la primera letra, recuerden que en programacion la primera letra o el primer numero
#se inicia desde el 0
'''
como queremos ver si coincide la primera letra o la ultima utilizaremos los operadores logicos.
en este caso utilizaremos el operador (or) ya que queremos ver si coincide la primera letra o=(or) la ultima
para saver cual es la ultima letra de un nombre se pone adentro de los corchetes [-1]
'''
#si nombre1 es igual a la primera letra del nombre 2 
#o si nombre 1 = a la ultima letra [-1] del nombre2
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    #que se imprima que si hay coincidencia de que si son iguales las letras
    print("Si hay Coincidencia")

    #si no hay concidencia que nos imprima de que no hay coincidencia
else:
    print("No hay coincidencia")