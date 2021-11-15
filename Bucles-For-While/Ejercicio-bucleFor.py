'''
Ejercicio para utilizar el bucle for.

*Crear un programa que muestre la sumatoria de todos los numeros
 entre el 0 y el 100.
'''
#creamos una variable llamada total, que la inicializaremos en = 0
total = 0
#utilizamos la funcion de rangos, para indicarle  el rango qu es del 0 al 100, 
# ponemos 101 por que en programacion se empieza a contar del 0
for i in range(101):
    #le decimos que nuestra variable total la igualaremos
    #entonces sera = a total + i osea 100 el numero de rango que nos pidieron
    total=total+i
    print("Sumatoria: ",total)








