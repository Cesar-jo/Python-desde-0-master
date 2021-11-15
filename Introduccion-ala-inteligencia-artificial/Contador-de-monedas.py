#Importamos la libreria de opencv
from cv2 import cv2
#importamos numpy y lo llamaremos = np, para solo llamar esta libreria por el nombre de np
import numpy as np
#lo que hara este valor o metodo gause sera tomar un cuadro de pixeles de 3x3 como el valor que le pusimos = 3
valorGause= 3 #=y ese cuadro que se formo de 3x3, va a quitar el ruido a la imagen pixel por pixel
Valorkernel= 3
#creamos una variable, donde se ubica la imagen que utilizaremos
path= r'C:\Users\ternu\OneDrive\Escritorio\curso-python\Introduccion-ala-inteligencia-artificial\monedascontorno\monedas.jpg'
imagen=cv2.imread(path) #con cv2.imread(path) le ldecimos que lea la imagen
#ahora pasamos la imagen a escalas de grises con la funcion .cvtColor
grises= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  #y la escala de gris que queremos = cv2.COLOR_BGR2GRAY
'''
Ahora vamos a quitarle el ruido a las imagenes para poder hacer un reconocimiento mejor
para ello utilizaremos en desemfoque gausiano osea un suaviante de imagen
para ello utilizamos la funcion cv2.GaussianBlur = para quitarle el ruido a las imagenes
'''
#utilizamos la funcion cv2.GaussianBlur = para quitarle el ruido a las imagenes
#(grises, (valorGause, Valorkernel), 0) 
# grises,= el primer valor pasaremos la imagen que convertimos a escalas de grises
#segundo valor pasaremos el valor de gause 
# = que es el desenfoque que queremos para la imagen que sera de 3
gause= cv2.GaussianBlur(grises, (valorGause, valorGause), 0)
'''
segunda eliminacion de ruidos, utilizaremos la funcion cv2.canny
que lo que hara es encontrar los bordes de una imagen
'''
#para ello utilizaremos la imagen de gause que eliminamos el ruido(gause,)
#y despues los valores de eliminacion de ruido que queramos (gause, 60, 100)
#lo que haran estos valores sera convertir en negra la imagen 
# y solo mostrar el contorno de las imagenes en color blanco para ver mejor su estructura,su forma o la persona
canny= cv2.Canny(gause, 60, 100)
'''Ahora utilizaremos a la lib de numpy que a numpy la llamamos = np
'''
#Ahora le decimos que contorno queremos que muestre, que es solo el contorno de afuera de las monedas
#eso se hace con la funcion .ones
#utilizaremos el valor de kernel, que sera de 3x3
#utilizaremos el valor de kernel, que sera de 3x3= que cra una matriz de 9 datos
#[1. 1. 1.]
#[1. 1. 1.]  = esta matris lo que hara sera rellenar los espacion basios de puntos o pixeles que le
#[1. 1. 1.]    falta a la imagen con la funcion .morphologyEx
kernel= np.ones((Valorkernel, Valorkernel),np.uint8) 
#con la funcion de numpy= cv2.morphologyEx
#que lo que hara esta funcion sera rellenar los espacion basios de una imagen con la matriz de .ones que creamos
#como primer valor pasamos la imagen(canny)
#agregamos la funcion cv2.MORPH_CLOSE = que cirve para limpiar el contorno de adentro de una imagen
#3ser valor: le aplicamos la matris cque creamos = kernel, para que trabaje con cv2.MORPH_CLOSE 
# para eliminar el contorno de adentro de una imagen
# rellenando de agujeros negros para que quede el contorno de afuera de la imagen osea el puro circulo de la moneda
cierre= cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
'''
Utilizaremos la funcion .findContours = que sirve para trazar o dibujar los contornos de una imagen,video,objeto
Su primer argumento es la imagen de origen = cierre
el segundo argumento son los contornos que deben pasarse como una lista de Python = cv.RETR_TREE
el tercer argumento es el método de aproximación de contorno = cv2.CHAIN_APPROX_SIMPLE  ó   cv2.CHAIN_APPROX_NONE
ejemplo= cv.findContours contornos, jerarquía = cv.findContours (umbral, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
'''
#El primer valor que le pasaremos sera la imagen = cierre
#El 2do como se va a mostrar, lo mostraremos como una listita de datos = cv2.RETR_LIST
#El tercero sra mostrar el metodo de contorno, existen 2 cv.CHAIN_APPROX_SIMPLE ó cv.CHAIN_APPROX_NONE
contornos, jerarquía=cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contornos)))
# imagen= nos piden como primer dato ingresar la imagen original
# contorno= los contornos que se han obtenidos, para ello importamos nuestra variable contorno
# 1´2´3´=etc =el nuemero de contornos a mostrar ó -1 = sirve para mostrar todos los contornos que tiene tu imagen)
#(0,255,0)=color verde =el color que quieres que aparesca como contorno
# 3= y por ultimo dato el grosor del contorno
'''cv2.drawContours(umbral, contorno, -1, (0,255,0), 2)
'''
cv2.drawContours(imagen, contornos, -1, (0,255,0), 2)



'''
Mostrar el resultado de la imagen
'''
#cv2.imshow("Imagen en grises", grises)
#cv2.imshow("Imagen en gause", gause)
#cv2.imshow("Imagen en canny", canny)
#cv2.imshow("cierre",cierre)
cv2.imshow("Resultado", imagen)
cv2.waitKey(0)