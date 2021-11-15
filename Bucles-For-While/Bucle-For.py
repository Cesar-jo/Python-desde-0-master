'''
BUCLE FOR = este ciclo re le conoce por recorrer datos en una coleccion, un array, una lista, etc
'''
#para crar un ciclo for, basta en lo siguiente
#agregamos un for, segido la variable de interaccion, esta variable le podemos poner como queramos
#para hacer mas limpio el codijo nuestra variable de interaccion sera (i)
'''
que va hacer esa variable de interaccion= i
lo que va hacer sera recorrer en nuestros datos del array (for i in data)
para que despues con un print, nos imprima los datos, que se almacenan en ese array
'''
#creamos un array que se llamara datos
data= [6,8,9,4,7,"hola","me llamo","Cesar"]
#y le decimos que i recorra en(in) data osea nuestro array para saver que contiene
for i in data:
#Utilizamos la f = para la salida de datos, en este caso los datos a sacar es del array
#e agregamos la variable de interaccion (i) para imprimir los datos del array
    print(f"Objeto : {i}")