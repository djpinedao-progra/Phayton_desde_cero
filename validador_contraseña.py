# --- Funciones auxiliares ---

def tiene_longitud(password):
    return len(password) >= 8

def tiene_mayuscula(password):
    for c in password:
        if c.isupper():
            return True
    return False

def tiene_digito(password):
    for c in password:
        if c.isdigit():
            return True
    return False

def tiene_especial(password):
    especiales = "!@#$%"
    for c in password:
        if c in especiales:
            return True
    return False

def sin_tres_repetidos(password):
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
    return True


# --- Función principal ---

def validar_password(password):
    return (
        tiene_longitud(password) and
        tiene_mayuscula(password) and
        tiene_digito(password) and
        tiene_especial(password) and
        sin_tres_repetidos(password)
    )

def diagnosticar_password(password):
    print(f"\nDiagnóstico para: '{password}'")
    errores = []

    if not tiene_longitud(password):
        errores.append("✗ Debe tener al menos 8 caracteres")
    if not tiene_mayuscula(password):
        errores.append("✗ Debe tener al menos una letra mayúscula")
    if not tiene_digito(password):
        errores.append("✗ Debe tener al menos un dígito")
    if not tiene_especial(password):
        errores.append("✗ Debe tener al menos un carácter especial (!, @, #, $, %)")
    if not sin_tres_repetidos(password):
        errores.append("✗ No puede tener 3 caracteres iguales seguidos")

    if errores:
        print("Contraseña INVÁLIDA:")
        for e in errores:
            print(" ", e)
    else:
        print("✓ Contraseña VÁLIDA")

    return len(errores) == 0


# --- Programa principal ---
password = input("Ingresa tu contraseña: ")
diagnosticar_password(password)

