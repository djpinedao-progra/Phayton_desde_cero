# --- Funciones de conversión base ---

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def fahrenheit_a_rankine(f):
    return f + 459.67

def rankine_a_fahrenheit(r):
    return r - 459.67


# --- Función principal ---

def convertir(valor, origen, destino):
    origen  = origen.upper()
    destino = destino.upper()

    if origen == destino:
        return valor

    # Primero convertimos todo a Celsius como escala intermedia
    if origen == "C":
        en_celsius = valor
    elif origen == "F":
        en_celsius = fahrenheit_a_celsius(valor)
    elif origen == "K":
        en_celsius = kelvin_a_celsius(valor)
    elif origen == "R":
        en_celsius = fahrenheit_a_celsius(rankine_a_fahrenheit(valor))
    else:
        print(f"Error: escala de origen '{origen}' no válida.")
        return None

    # Luego convertimos de Celsius a la escala destino
    if destino == "C":
        return en_celsius
    elif destino == "F":
        return celsius_a_fahrenheit(en_celsius)
    elif destino == "K":
        return celsius_a_kelvin(en_celsius)
    elif destino == "R":
        return fahrenheit_a_rankine(celsius_a_fahrenheit(en_celsius))
    else:
        print(f"Error: escala de destino '{destino}' no válida.")
        return None


# --- Programa principal ---
ESCALAS = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin", "R": "Rankine"}
SIMBOLOS = {"C": "°C", "F": "°F", "K": "K", "R": "°R"}

print("=== Conversor de Temperaturas ===")
print("Escalas disponibles: C (Celsius), F (Fahrenheit), K (Kelvin), R (Rankine)")

valor  = float(input("\nIngresa el valor: "))
origen  = input("Escala de origen  (C/F/K/R): ").upper()
destino = input("Escala de destino (C/F/K/R): ").upper()

resultado = convertir(valor, origen, destino)

if resultado is not None:
    print(f"\n{valor}{SIMBOLOS[origen]} ({ESCALAS[origen]})")
    print(f"  → {resultado:.2f}{SIMBOLOS[destino]} ({ESCALAS[destino]})")
    