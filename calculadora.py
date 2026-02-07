

numero_1  = int ( input ("Ingrese el primer npumero:"))
numero_2 = int (input ("Ingrese el segundo numero:"))

print("Seleccione una opción a realizar:")
print("Sus opciónes son las siguintes:")
print("Suma: +")
print("Resta: -")
print("Multiplicación: *")
print("División: /")
operacion = input ("ingrese el simbolo de la opreración a realizar: 77")

if operacion =="+":
   print(f"resultado: {numero_1 + numero_2}")
elif operacion =="-":
   print(f"resultado: {numero_1 - numero_2}")
elif operacion =="*":
   print(f"resultado: {numero_1 * numero_2}")
elif operacion =="/":
   print(f"resultado: {numero_1 / numero_2}")
else:
   print("Operación no válida")

print ("No se si funcionno")

 

