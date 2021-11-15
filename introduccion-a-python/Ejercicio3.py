'''
Ejercicio numero 3. Encontrar el radio y longitud de un circulo
'''
#importamos la libreria de mat para trabajar con valores de pi *, raizes cuadradas y operaciones complejas
import math


# para poder hacer este ejecicio, devemos saver la formula de pi
# que en el ejercicio nos dice que area es igual a π*r² 

'''
fomula: nos dan los valores de :
area = π*r²
y longitud es = 2*π*r
'''
# creamos el dato de entrada para que sea igual al valor de  radio y nos saque, 
# nos encuentre el area y la longitud
r=float(input("Ingrese el radio: "))
#Entonces creamos las variables con sus respectivos datos
#area es igual a pi x radio al cuadrado
area = math.pi*r**2
longitud = 2*math.pi*r

# Cundo le agregamos esto :.1f  a nuestra variable area, 
# le indicamos la cantidad de decimales que queremos que nos aparesca
print(f"ingrese el area: {area:.1f}")
print(f"ingrese la longitud: {longitud:.1f}")