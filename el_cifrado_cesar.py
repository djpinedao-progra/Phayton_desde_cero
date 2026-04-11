# --- Funciones ---

def cifrar_caracter(c, desplazamiento):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + desplazamiento) % 26 + base)
    return c

def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)

def fuerza_bruta(mensaje_cifrado):
    print("\n--- Fuerza Bruta (26 desplazamientos) ---")
    for d in range(1, 27):
        intento = descifrar_mensaje(mensaje_cifrado, d)
        print(f"  Desplazamiento {d:>2}: {intento}")


# --- Programa principal ---

print("=== Cifrado César ===")
print("1. Cifrar mensaje")
print("2. Descifrar mensaje")
print("3. Fuerza bruta")

opcion = input("\nElige una opción (1/2/3): ")

if opcion == "1":
    mensaje      = input("Ingresa el mensaje: ")
    desplazamiento = int(input("Desplazamiento (1-25): "))
    cifrado = cifrar_mensaje(mensaje, desplazamiento)
    print(f"\nMensaje original : {mensaje}")
    print(f"Mensaje cifrado  : {cifrado}")

elif opcion == "2":
    mensaje        = input("Ingresa el mensaje cifrado: ")
    desplazamiento = int(input("Desplazamiento usado al cifrar: "))
    descifrado = descifrar_mensaje(mensaje, desplazamiento)
    print(f"\nMensaje cifrado   : {mensaje}")
    print(f"Mensaje descifrado : {descifrado}")

elif opcion == "3":
    mensaje = input("Ingresa el mensaje cifrado: ")
    fuerza_bruta(mensaje)

else:
    print("Opción no válida.")