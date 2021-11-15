from cv2 import cv2
import numpy as np # esta libreria son para trabajar con matrices
#creamos una funcion(def) para ordenar puntos
def ordenarpuntos(puntos):
#con esta funcion=.concatenate LO QUE HACEMOS ES UNIR, ENLAZAR MATRICES, osea los contornos que se encuentren en la imagen
    #adentro de los () pondremos el numero de matrices que queremos, en este caso seran 4
    #y cada matris se llamara puntos[] ya que ese es el valor que devolveremos con la funcion
    #y al ultimo agregamos un .tolist para converti esas matrices en una lista
    n_puntos=np.concatenate(puntos[0], puntos[1], puntos[2], puntos[3]).tolist()
    #ahora trabagaremos con cordenadas que x= a izquierda a derecha e y= de arriba hacia abajo
    #utilizaremos la funcion sorted = que lo que hace es ordenar arrays, listas,tuplas etc.
    #entonces le decimos que ordene  los puntos que creamos = n_puntos
    #vamos a utilizar la funcion Key=lambda = que lo que hace es reconocer lo que queremos ordenar
    #para ello le decimos a lambda que queremos ordenar
    #y lo que queremos ordenar seran nuestros puntos = n_puntos
    #que lecimos que n_puntos queremos que ordene la matris que va del 0 hasta el 1 = :n_puntos[1]
    y_order= sorted(n_puntos, Key=lambda n_puntos:n_puntos[1])
    #le decimos que x1_order sera igual = y_order y esta va a recorrer de la pocicion 0 = inicial
    #hasta la posicion 1
    #pero pusimos  y_order[0:2] del 0 al 2 por que asi se deve de poner, por que se deve de restar un valor
    #si ponemos del 0 al 2 [0:2] va a restar un valor ala ultima pocision que indicamos 2-1 =1 = [0:1]
    x1_order= y_order[0:2]
    #vamos a ordenar a x1_order con las funciones sorter y key=lambda para indicar que queremos ordenar
    #y le decimos que x1_order:x1_orden que lo ordene hasta el valor 0
    x1_order=sorted(x1_order, Key=lambda x1_order:x1_order[0])
    #le decimos que nuestra var x2_order sera = y_order ,que queremos que ordene los puntos
    #desde la pocicion 2 a la 3 = [2:4] = el ultimo valor se resta 4-1= 3 = [2:3]
    x2_order= y_order[2:4]
    #ahora vamos a ordenar x2_order que queremos que ordene x2_order:x2_order[0] de apartir del centro
    x2_order= sorted(x2_order,Key=lambda x2_order:x2_order[0])
    #le pedimos que nos retornen, todos estos valores pero ya ordenados
    return [x1_order[0], x1_order[1],x2_order[0],x2_order[1]]

    '''
    Creamos una funcion para alinear
    '''
     #a esta funcion le vamos a pedir 3 parametros= una imagen, un ancho y un largo
def alineamiento(imagen, ancho, alto):
    imagen_alineada=None
    grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #pasamos la imagen a escalas de grises
    _,resul_umbral=cv2.threshold(grises, 150,255, cv2.THRESH_BINARY)#ahora transformamos a B&W la imagen
    cv2.imshow("Este es nuestro Umbral", resul_umbral)#Con la funcion .imshow mostramos la imagen
     #ahora vamos a obtener los contornos con= cv2.findContours
    #para ello les pasamos los siguientes parametros (la imagen en escalas de grises)
    #cv2.RETR_EXTERNAL = utilizamos esta funcionpor que vamos a utilizar imagenes externas osea una camara 
     #despues le pasamos el tipo de contorno que trabajaremos que sera un = cv2.CHAIN_APPROX_SIMPLE
    #y al final le decimos que [0] = sera nuestro primer orden
    contorno,jerarquia= cv2.findContours(resul_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    #ahora vamos a ordenar los contornos con sorted y con key le indicamos que queremos ordenar
    #y lo que ordenaremos sera el area del contorno = Key=cv2.contourArea
    #revese = True = lo que hace es ordenar de menor a mayor los puntos
     #y con [0:1] le decimos que ordene los puntos desde el orden 0 hasta el 1 = que sera para el valor de las x
    contorno=sorted(contorno,Key=cv2.contourArea, revese=True)[0:1]
    for i in contorno: #le decimos que nuestro interador= i recorra en contornos para sacra informacion
#Con la funcion cv2.arcLength sacamos el area, osea medir las curvas de las formas que vea con la camara o imagenes
    #le pasamos nuestro interador (i, que lo que hara es traer y recorrer todos los contornos para medir el area o las curvas)
    #y le pasamos un true, por que ahi va la funcion de cerrar, y con el true le decimos que cierre
        epsilon=0.01*cv2.arcLength(i, True)
        #haremos un aproximado con la funcion = cv2.approxPolyDP
        #parra ellos le pasamos nuestra variable de interacion i
        #  que va a traer todas las curvas alladas, osea los contornos
        #le pasamos nuestra var epsilon que lo que hara es sacar la area, las curvas
        #y le decimos que si esto va a cerrar y le decimos que si = True
        aprox=cv2.approxPolyDP(i, epsilon, True)
        #le decimos que si tiene 4 puntos nuestro aprox, osea nuestros contornos, que con las matrices
        #le dimos 4 puntos para que mida las curvas o el area de lo objetos esos 4 puntos=listas
        if len(aprox)==4:
            #si tiene 4 puntos, entonces puntos sera = a ordenar puntos
            #que nuestra variable ordenar puntos, hicimos que nuestros puntos
            #se ordenen en planos cartecianos para medir
            #osea en plano carteciano en forma de cruz +
            #y le pasamos nuestro aprox, que son los 4 puntos
            puntos=ordenarpuntos(aprox)
            #con la funcion .float32 convertimos (puntos) de las matrices a numeros enteros y ya no en decimales .0
            puntos1=np.float32(puntos)
            #ahora colocaremos los puntos en las esquinas , para que mida en foma de un cuadrado o rectangulo
            puntos2=np.float32([0,0],[ancho,0],[0,alto],[ancho,alto])
            # vamos a trabajar las prespectivas para que cuando se mueva la imagen siga la imagen 
            #para ello utilizamos la funcion cv2.getPerspectiveTransform
            M = cv2.getPerspectiveTransform(puntos1, puntos2)
            #con la funcion cv2.wrapPerspective es para pasarle la informacion para la perpctiva de la imagenes
            #le pasamos como parametros,(las imagenes) las prespectivas(m) que son los puntos para los contornos
            #y la medicion de nuetros puntos
            imagen_alineada= cv2.wrapPerspective(imagen, M, (ancho,alto))
 #que nos retorne la imagen alineada para las prespectivas que no cambie si se muev el objeto o la camara
    return imagen_alineada
capturavideo= cv2.Videocapture(0)

while True:
    tipocamara,camara=capturavideo.read()
    if tipocamara==False:
        break
    imagen_A6=alineamiento(camara,ancho=480,alto=640)
    if imagen_A6 is not None:
        puntos=[]
        imagen_gris=cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagen_gris,(5,5),1)
        _,umbral2=cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbral",umbral2)
        contorno2=cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6, contorno2, -1, (255,0,0),2)
        suma1=0.0
        suma2=0.0
        for c_2 in contorno2:
            area=cv2.contourArea(c_2)
            Momentos = cv2.moments(c_2)
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])

            if area<9300 and area>8000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6, "S/. 0.20",(x,y) , font, 0.75, (0,255,0),2)
                suma1=suma1+0.2
            
            if area<7800 and area>6500:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6, "S/. 0.10",(x,y) , font, 0.75, (0,255,0),2)
                suma2=suma2+0.1
        total=suma1+suma2
        print("Sumatoria total en Centimos:",round(total,2))
        cv2.imshow("Imagen A6", imagen_A6)
        cv2.imshow("camara", camara)
    if cv2.waitKey(1) == ord('s'):
        break
capturavideo.release()
cv2.destroyAllWindows()






