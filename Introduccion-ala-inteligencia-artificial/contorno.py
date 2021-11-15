from cv2 import cv2
#creamos una variable llamda PHAT
#Que path = a la ruta donde se encuentra la imagen para practicar reconocimientos de objetos
# phat sera = a r que r= significa leer archivo
#despues de la seguido de las comillas simples '' va nuesta ruta
path= r'C:\Users\ternu\OneDrive\Escritorio\curso-python\Introduccion-ala-inteligencia-artificial\monedascontorno\contorno.jpg'
#creamos una variable llamada imagen = que sera igual a la funcion de la libreria cv2.imread
#que la funcion .imread, sirve para leer imagenes
# segido de los corchetes () ira la imagen a leer, osea nuestra ruta donde se encuentra la imagen
imagen=cv2.imread(path)
#Ahora vamos a convertir nuestra imagen a escalas de grises
#para ello utilizamos la funcion .cvtColor,
# segido de (imagen,) la ruta de la imagen que queremos poner en color gris
#segido del color a convertir (cv2.COLOR_BGR2GRAY) que es un color gris
grises= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# con nuestra funcion threshold, importamos las escalas de grises a utilizar para ello ocuparemos 3 parametros
#la imagen a convertir,la escala minima de umbrales y la escala maxima a utilizar
#  ejemplo: (imagen= importamos la imagen,100= escala minima,255= escala maxima a utilizar)
#y por ultimo el tipo de humbral a utilizar, 
# que nosotros utilizaremos el blanco y negro osea el umbral binario = cv2.THRESH_BINARY
'''
pondremos dos variables, una se refiere al tipo de umbral que se utilizo, 
osea cuando la convertimos a escala de grises, poreso nuestra variable grises
y la segunda seria al umbral que convertimos que seria binaria osea blanco y negro
'''
tipoumbral,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

'''
Utilizaremos la funcion .findContours = que sirve para trazar o dibujar los contornos de una imagen,video,objeto
Su primer argumento es la imagen de origen = umbral
el segundo argumento son los contornos que deben pasarse como una lista de Python = cv.RETR_TREE
el tercer argumento es el método de aproximación de contorno = cv2.CHAIN_APPROX_SIMPLE  ó   cv2.CHAIN_APPROX_NONE
ejemplo= cv.findContours contornos, jerarquía = cv.findContours (umbral, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
'''
#El primer valor que le pasaremos sera la imagen = umbral
#El 2do como se va a mostrar, lo mostraremos como una listita de datos = cv2.RETR_LIST
#El tercero sra mostrar el metodo de contorno, existen 2 cv.CHAIN_APPROX_SIMPLE ó cv.CHAIN_APPROX_NONE
contorno,jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#ahora lo que vamos hacer sera dibujar en el contorno de nuestra imagen
#Para ello vamos a utilizar la funcion cv2.drawContours, para dibujar contornos
#Que como parametros nos piden:
# imagen= como primer dato, nos pide la imagen original
# contorno= los contornos que se han obtenidso, para ello importamos la variable contorno que tenemos
# 1´2´3´=etc =el nuemero de contornos a mostrar ó -1 = sirve para mostrar todos los contornos que tiene tu imagen)
#(0,255,0)=color verde =el color que quieres que aparesca como contorno
# 3= y por ultimo dato el grosor del contorno
'''cv2.drawContours(umbral, contorno, -1, (0,255,0), 3)
'''
cv2.drawContours(imagen, contorno, -1, (0,255,0), 3)



'''
Esto de abajo sirve para mostrar una imagen
'''
#ahora para mostrar la imagen utilizamos la funcion .imshow
#segido de la variable (imagen) donde ahora se encuentra la ruta donde se aloja nuestra imagen a mostrar
cv2.imshow('Imagen original',imagen)
#cv2.imshow('Imagen en grises',grises)
#cv2.imshow('Imagen umbral',umbral)
#Ahora mara mostrar la imagen estaticamente, osea que se quede la imagen hasta que nosotros queramos cerrarla
#utilizaremos la funcion .waitKey(0) para que como su nombre lo dice wait=nos espere la imagen
#y con el numero (0)le indicamos que este estatica la imagen,
#  si le ponemos un (1) solo durara un segundo la imagen a mostrar, se le pone uno para ver un video en tiempo real
#osea grabandote
cv2.waitKey(0)
#ahora le decimos con la funcion .destroyAllWindows()
#como su nombre lo dice destruir todas las ventanas emergentes cuando le demos click en - o x de cerrar
cv2.destroyAllWindows()