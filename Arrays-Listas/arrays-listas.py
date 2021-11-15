'''
Bucles - Listas
'''

#para hacer un array, primero declaramos una variable y abrimos corchetes[]
# para que adentro escribamos el contenido del array

array = ["Juegos", "PC", 18.00, 18, [6, 7, 10.4], True, False]
#para imprimir todos los datos guardados del array,
#solo es cuetion de llamar la variable array en nuestro print(array)
print(array)
#si queremos llamar solo un dato que este guardado en nuestro array lo hacemos de la siguiente manera:
#recuerden que en programacion se cuentan los datos desde el 0, en este caso tenemos 7 datos
#pero son 6 como tal ya que el primer dato vendria hacer 0 = Juegos 1= pc 2= 18.00, etc
'''
para llamar un solo dato del array solo llamamos nuestro array en nuestro print, 
seguido del numero del dato en el que se encuentra adentro de los [] ejemplo print(array[1])  1=PC
'''
print(array[1])

#si queremos sacar el ultimo dato recuerden que se utilizan numeros negativos, ejemplo print(array[-1])
#el -1 seria nuesto ultimo dato del array que seria = False
'''
si quiere mostrar el ultimo dato seria [-1]
si quiero mostrar el penultimo dato seria [-2]
si quiero mostrar el antepenultimo dato seria [-3]
etc.
'''
print(array[-1])

'''
si queremos sacr un dato desde el primero hasta el tercero guardado seria
asi [0:2] 0= al primer dato : = hasta y el 2 seria el 3ser dato
pero no traera el segundo dato que sera 18.0 ya que solo pedimos que nos traiga 
los primeros dos datos con el [0:2], si queremos sacra el tercer dato seria [0:3]
'''

print(array[0:3])

#si queremso que nos traiga datos del 1 al 4
print(array[1:4])

#si queremso imprimir del primer dato hata el ultimo sera asi [ : ] o asi = [0: ]
print(array[0:])