from cv2 import cv2

path= r'C:\Users\ternu\OneDrive\Escritorio\curso-python\Introduccion-ala-inteligencia-artificial\monedascontorno\contorno.jpg'
imagen=cv2.imread(path)
#utilizamos la funcion .cvtColor, para convertir la imagen a una escala de grises
#(imagen,)=  la ruta de la imagen que queremos poner en color gris, osea nuestra variable donde se aloga la Imagen
#segido del color a convertir (cv2.COLOR_BGR2GRAY) que es un color gris
grises= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
'''
pondremos dos variables, una se refiere al tipo de umbral que se utilizo, 
osea cuando la convertimos a escala de grises, poreso nuestra variable grises
y la segunda seria al umbral que convertimos que seria binaria osea blanco y negro
'''
tipoumbral,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
#El primer valor que le pasaremos sera la imagen = umbral
#El 2do como se va a mostrar, lo mostraremos como una listita de datos = cv2.RETR_LIST
#El tercero sra mostrar el metodo de contorno, existen 2 cv.CHAIN_APPROX_SIMPLE ó cv.CHAIN_APPROX_NONE
contorno,jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# imagen= nos piden como primer dato ingresar la imagen original
# contorno= los contornos que se han obtenidos, para ello importamos nuestra variable contorno
# 1´2´3´=etc =el nuemero de contornos a mostrar ó -1 = sirve para mostrar todos los contornos que tiene tu imagen)
#(0,255,0)=color verde =el color que quieres que aparesca como contorno
# 3= y por ultimo dato el grosor del contorno
'''cv2.drawContours(umbral, contorno, -1, (0,255,0), 3)
'''
cv2.drawContours(imagen, contorno, -1, (0,255,0), 3)

'''
Esto de abajo sirve para mostrar una imagen
'''
#.imshow = sirve para mostrar la imagen
cv2.imshow('Imagen original',imagen)
#.waitKey = sirve par mostrar el tiempo a visualizar la imagen
#  (0)con el cerpo le indicamos que este estatica la imagen hasta que le demos en cerrar
cv2.waitKey(0)
#.destroyAllWindows() = sirve para destruir todas las ventanas cuando le demos en - 0 x para cerrar
cv2.destroyAllWindows()