# Pedimos los datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
ciudad = input("Ingresa tu ciudad: ")
hobby = input("Ingresa tu hobby favorito: ")

# Línea separadora para la tarjeta
separador = "-" * 40

# Mostramos la tarjeta de presentación
print("\n" + separador)
print("        TARJETA DE PRESENTACIÓN")
print(separador)
print(f"Nombre : {nombre}")
print(f"Edad   : {edad}")
print(f"Ciudad : {ciudad}")
print(f"Hobby  : {hobby}")
print(separador)
