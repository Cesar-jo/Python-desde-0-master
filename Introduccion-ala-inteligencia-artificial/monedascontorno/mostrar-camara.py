from cv2 import cv2
#esta funcion .VideoCapture(0) = sirve para buscar camarasque esten trabajando en la pc
# si ponemos 1 .VideoCapture(1) = sirve para trabajar con camaras externas como camaras de seguridad etc
capturavideo=cv2.VideoCapture(0)
#le decimos que si no se encontro una camara(capturavideo) o si no esta abierta una camara(.isOpened())
if not capturavideo.isOpened():
    #que nos imprima que no ha encontrado ninguna camara
    print("No se encontro una camara")
    #y cerramos
    exit()
#WHILE = MIENTRAS QUE
#le decimos mientras que la camara tenga un valor true = verdadero, osea que si se encontro una camara
while True:
    #nos va a leer con la funcion .read() si hay una camara = capturavideo
    tipocamara, camara= capturavideo.read() 
    #Esto es opcional. qahora pasamos la imagen a escalas de grises con la funcion .cvtColor
    grises= cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY)  #y la escala de gris que queremos = cv2.COLOR_BGR2GRAY
    #con la funcion .imshow hacemos que nos aparesca la camara 
    cv2.imshow("Camara/En vivo",grises) 
    #con la funcion .waitKey que se refiera a la duracion de la camara 
    # que pusimos .waitKey(1) por que es en tiempo real
    #le decimos que si whaitkey es 1 .waitKey(1)=osea usar la camara en tiempo real
    #que sea == a la funcion ord que lo que hace es poder cerrar la grabacion con la letra que queramos = letra q
    if cv2.waitKey(1)== ord("q"):
        #y con el break cerramos si se cumple esa orden de precionar la letra q
        break 

capturavideo.release()
cv2.destroyAllWindows()
