'''
Dados de Conjuntos. Algebra, Matematicas
u = union 
En python la union se representa asi = |
'''

#A u B,  A u C
A={1,2,3,4}
#B u C
B={2,3,5,6}  
C={3,4,6,7}

# imprimimos la unios de A Y B = A u B
#La union en python se reprecenta asi = | = A|B
print(A|B)
# imprimimos la unios de A Y C = A u C
print(A|C)
# imprimimos la unios de B Y C = B u C
print(B|C)

'''
Ahora veremos las interseciones de conjuntos = ∩ Python = &
Union de conjuntos = u        Python union de conjuntos = " | "

interseciones de conjuntos = ∩    Python interseccion de conjuntos = " &  "
'''
#haremos una interseccion de A ∩ B
print(A&B)
#haremos una interseccion de A ∩ C
print(A&C)
#haremos una interseccion de B ∩ C
print(B&C)

'''
Ahora veremos Como saver que elementos no tiene por ejemplo A Y B
para ello usamos el signo " - " = A - B
'''
#imprimimos los elementos que no tiene A NI B
print(A-B)
#imprimimos los elementos que no tiene c NI B
print(C-B)

'''
Ahora para saver que datos se intersectac utilizamos la tilde  ^
ejemplo = A^B
'''
print(A^B)
