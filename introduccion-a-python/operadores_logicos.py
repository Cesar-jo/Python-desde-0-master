'''
OPERADORES LOGICOS
(and=  se cumple a y b,  or= se cumple a or b  y  not = no a) = and = y, or = o y not = no
para usar los operadores logicos se ejecutan mediante parentecis de la siguiente manera (() aqui va el operador logico ())
                                                                                            and, or, not
'''
#HACEMOS LAS COMPARACIONES
#le lecimos que a es menoe que b y si c es mayor que b
#para ese tipo de condicionales deve de cumplir lque sean igaul osea que sea verdad cada condicion para que nos arroge un valor
# de true, si uno de esos condiciones es falsa y la otra verdad nos saldra un false ya que deven de cumplir lo mismo los dos operadores o condicionales
a=30
b=40
c=50
r =  ((a<b) and (c>b))
print(r)

'''
si usamos la negacon, nos va a negar todo lo que le indiquemos
'''
a=30
b=40
c=50
r =  not((a<b) and (c>b))
print(r)





