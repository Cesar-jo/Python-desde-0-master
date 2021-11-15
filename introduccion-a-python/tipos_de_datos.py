#tipos de datos en python
#veremos los datos de tipo Entero, de Texto, Boleanos
#------------------------------------------------------------------

#En python no se maneja las variables como en java, aqui se asignan valores
#ejemplo: en java se asignava asi las variable, como tipo de dato y el nombre de la variable
# ejempo int numero;
#------------------------------------------------------------------

#en python es asi se le asigna un valor, ejemplo: numero = 50 y ya imprimimos ese valos como print (numero)
#empezamos con los tipos de tados enteros INT
#esa es la facilidad de python, ya no tengo que decirle que tipo de dato es si int, boleano,string etc
#ya que python analiza que tipo de dato es para despues imprimirlo

numero = 50
print(numero)
#vamos a utilizar la funcion type, para saver que tipo de dato es el que nos bota
#le decimos que nos imprima el tipo de dato que estamos trabajando en uestra variable numero
print(type(numero))

#haremos lo mismo, pero ahora trabajaremos con los tipos de datos de datos float decimales

nuemb = 50.6
print(nuemb)
print(type(nuemb))

#Ahora trabajaremos con el tipo de dato texto, osea string (str)
#para este dato se lo asignamos el vamos con "" las comillas dobles o  simples ''
palabra = "César" 'José'
print(palabra)
print(type(palabra))

#ahora trabajaremos con los tipos de datos boleanos(bool) que hay dos que son true o false verdad o falso

datot= True
print(True)
print(type(True))

datof= False
print(False)
print(type(False))


#Ahoar ya viendo los tipos de datos haremos una operacion de sumas, para ver como se hace en python
#como vemos aqui en py ya bo se declara el tipo de dato si no solo damos los valores

#para ello le damos el valor al numero 1 y al numero 2
n1= 120
n2=12.8
#despues declaramos que queremos sumar el numero 1 y el dos y despues imprimimos esa declaracion
suma=n1+n2
print("Resultado:", suma)

#En python es muy facil hacer las operaciones de suma, resta y multiplicacion como podemos ver
#aolo es cuestion de cambiar su signo para indicar que operacion hacer
# *= multiplicacion /=division -=resta +=suma

#multiplicacion

n1= 2
n2= 5
multiplicacion=n1*n2
print("Resultado:", multiplicacion)


#divicion

n1= 10
n2= 2
divicion=n1/n2
print("Resultado:", divicion)


#tambien podemos cambiar los tipos de datos , los valores ya asignados, esa el la flexibilidad de python
#ejemplo

dato=60
print(dato)
dato="cambio de valor"
print (dato)