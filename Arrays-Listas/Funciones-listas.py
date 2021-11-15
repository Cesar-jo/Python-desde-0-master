'''
Funciones en listas
'''

array = ["Juegos", "PC", 18.00, 18, [6, 7, 10.4], True, False]
#Con el (len) nos cuenta cuantos elementos tenemos en nuestro array
print(len(array))
#con el la funcion append lo que hace es agregar otro dato al ultimo en nuestro array
#ejemplo= llamamos nuestra variable array despues de la funcion y el dato a agregar
#array.append("Nuevo dato")
array.append("nuevo dato")
array.append(66)
#print(array)
'''
ahora si queremos agregar un dato en cualquier pocicion de nuestro array seria:
con la funcion insert = a insertar datos, segido ()
y adentro ira en que dato quieres que valla el nuevo dato a registrar 
segido de una coma y despues el dato a registrar
ejemplo= array.insert(1,"segundo nuevo dato") si es numero array.insert(1, 66)
'''
array.insert(1,"segundo nuevo dato")
array.insert(2,88)
print(array)

'''
Ahora si queremos agregar un nuevo bloque pero al final
utilizaremos la funcion .extend() y adentro de los () agregaremos unos [] asi ([])
para que adentro de ([]) valla el nuevo bloque a agregar.
 quedaria asi = array.extend(["hola", 55, "Cesar", 44.9])
'''
array.extend(["hola", 55, "Cesar", 44.9])
print(array)

'''
Ahora veremos como concatenar arrays.
para ello creamos 2 arrays con sus respectivas variables
'''
array1= ["Hola", "Me llamo", "cesar y tengo", 20 , "años"]
array2= ["Estudio", "La carrera de:", "ING.Software y sistemas", 20 ,]
#ahora para concatenar arrais osea unirlos, 
# seria asi= crear otra variable y sumar el array1 y array2,
#  para despues imprimir la nueva variable, ejemplo: array3 = array1 + array2
array3 = array1 + array2
#y imprimimos la nueva variable que tiene concatenadas mis dos arrays
print(array3)

'''
Ahora veremos el tema de buscar datos en un array
para ello lo hacemos con un print segido del dato a buscar y adonde deve de buscarlo asi = in arry
ejemplo = print("Hola" in lista)
'''

lista = ["Hola",20,40, "Cesar"]
#si halla el dato nos imprimira un true, de lo contrario un false si no lo haya
print("Hola" in lista)

'''
Ahora veremos como buscar un dato en un array y saver en que pocicion esta
para ello utilizaremos la funcion index. segido de la palabra o dato a buscar
ejemplo = print(lista.index("Hola"))
'''
lista = ["Hola",20,40, "Cesar"]
print(lista.index(20))


'''
Ahora veremos buscar cuantas veces se repite un dato en nuestro arry
para ello utilizaremos la funcion count. segido de la palabra o dato a buscar
ejemplo = print(lista.count("Hola"))
'''
lista = ["Hola",20,40, "Cesar",20,"Hola",20]
#vamos a contar cuantas veces se repite el numero 20 en nuesto array de lista y nos lo imprimira
print(lista.count(20))
#vamos a contar cuantas veces se repite el "Hola" en nuesto array de lista y nos lo imprimira
print(lista.count("Hola"))

'''
Ahora veremos como borrar un dato en un array.
para ello utilizaremos la funcion .remove  segido de las palabras o dato a elimina
ejemplo = lista.remove("Hola") y imprimimos nuestro array para  verificar si se eliminaron print(lista)
'''
lista = ["Hola",20,40, "Cesar",20,"Hola",20]
#solo va a elimir un sulo dato que le indiquemos
lista.remove("Hola")
print(lista)

'''
ahora para limpira un array y dejarlo vario.
se utiliza la funcion clear
ejemplo= lista.clear() y imprimimos nuestro array para ver si si limpio los datos
'''
lista = ["Hola",20,40, "Cesar",20,"Hola",20]
lista.clear()
print(lista)

'''
ahora para vamos a cambiar de pocicion los datos.
se utiliza la funcion .reverse()
ejemplo= lista.reverse() 
lo que hara es cambiar el primer dato hasta el ultimo y el ultimo dato hasta el principio
'''
lista = ["Hola",20,40, "Cesar",20,"Hola",20]
lista.reverse()
print(lista)

'''
ahora vamos a ordenr los datos de forma acendente, osea del menor al mayor.
Para ello se utilizara la funcion .sort()
ejemplo= numeros.sort() 
lo que hara es ordenar los del menor al mayor
'''
numeros = [37,20,40, 15,-7,0,10]
numeros.sort()
print(numeros)

'''
ahora vamos a ordenr los datos del mayor al menor.
Vamos a utilizar la funcion .sort(reverse=True) igual pero adentro de los () ira (reverse=True)
ejemplo= numeros.sort(reverse=True) 
lo que hara es ordenar los del mayor al menor
'''
numeros = [37,20,40, 15,-7,0,10]
numeros.sort(reverse=True) 
print(numeros)
