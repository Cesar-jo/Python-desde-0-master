'''
OPERADORES RELACIONALES
SON = (== ES IGUAL QUE, != DISTINTO QUE, < : MENOR QUE, <= : MENOR O IGUAL QUE, >: MAYOR QUE; >= : MAYO O IGUAL QUE)
'''


'''
operador igualitario ==
'''
#vamos hacer la comparacion con == que es de igualdad, para saver si 50 es = a 100, que nos arrogara un false de falso
r=50 == 100
print(r)
#vamos hacer la comparacion con == que es de igualdad, para saver si 100 es = a 100, 
# que nos arrogara un true de verdadero por que si son iguales
t=100 == 100
print(t)


'''
operador de negacion que es de distinto que !=
'''
#le decimos que ahora 50 ya no es igual a 50 con este operador para que niegue que 50 no es = a 50
r=50 != 50
print(r)

'''
operador < menor y menor o igual que <=
'''
#le decimos que si 50 es menor que 50, y esto nos arrogara un false ya que no es menor a 50
r=50 < 50
print(r)

#pero si decimos que si 50 es menor a 100 nos arrogara un true de verdad
t=50 < 100
print(t)

#ahora con el menor o igual que primero compara si un numero es menor al otro, si no es igual nos arroga un false
#y despues compara si es igual y nos arrogara un true
i= 150 <= 150
print(i)


'''
operador > mayor y menor o igual que >=
este funciona igual que el menor o igual que pero al reves
primero verifica si es mayor a un numero y despues si es igual
'''
#le decimos que si 50 es mayor que 50, y esto nos arrogara un false ya que no es mayor a 50
r=50 > 50
print(r)

#pero si decimos que si 100 es mayor a 50 nos arrogara un true de verdad
t=100 > 50
print(t)

#ahora con el mayor o igual que primero compara si un numero es mayor al otro, si no es mayor nos arroga un false
#y despues compara si es igual y nos arrogara un true
i= 160 <= 160
print(i)