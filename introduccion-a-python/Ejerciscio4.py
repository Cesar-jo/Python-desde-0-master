'''
Ejercicio 4. Obtener el precio final que se tiene que pagar si se aplica
el 36% de descuento total de la compra
'''

precioincial = float(input("Ingrese el precio: "))
#Para aplicar el 36% de descuento total de la compra
#se deve de hacer lo siguiente
#Antes de empezar el 36% se calcula asi 36/100

#para obtener el precio fina necesitamos  sacar primero el descuento, 
# para ello multiplicamos el precio inicial * el 36% de descuento
descuento=precioincial*(36/100)
#ahora si para sacr el precio final se tiene que restar el precio anterio con el descuento
preciofinal= precioincial - descuento

print(f"El precio final es de: MX/ {preciofinal:.2f}")

