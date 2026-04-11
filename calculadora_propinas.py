# --- Historial de operaciones ---
historial = []

# --- Funciones de cálculo ---

def calcular_propina(subtotal, porcentaje):
    return subtotal * porcentaje / 100

def calcular_total(subtotal, propina):
    return subtotal + propina

def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: el número de personas debe ser mayor a 0."
    return total / personas

def aplicar_descuento(subtotal, descuento_pct):
    descuento = subtotal * descuento_pct / 100
    return subtotal - descuento


# --- Menú ---

def mostrar_menu():
    print("\n" + "=" * 40)
    print("       RESTAURANTE EL BUEN SABOR")
    print("=" * 40)
    print("  1. Calcular propina")
    print("  2. Dividir la cuenta")
    print("  3. Aplicar descuento + propina")
    print("  4. Resumen de operaciones")
    print("  5. Salir")
    print("=" * 40)


# --- Opciones ---

def opcion_propina():
    try:
        subtotal = float(input("\n  Ingresa el subtotal: Q"))
        print("  Propinas sugeridas: 10% | 15% | 20%")
        porcentaje = float(input("  Porcentaje de propina: "))

        propina = calcular_propina(subtotal, porcentaje)
        total   = calcular_total(subtotal, propina)

        print(f"\n  Subtotal : Q{subtotal:.2f}")
        print(f"  Propina  : Q{propina:.2f}  ({porcentaje}%)")
        print(f"  Total    : Q{total:.2f}")

        historial.append(f"Propina {porcentaje}% sobre Q{subtotal:.2f} → Total Q{total:.2f}")

    except ValueError:
        print("  Error: ingresa solo números.")

def opcion_dividir():
    try:
        total   = float(input("\n  Ingresa el total a dividir: Q"))
        personas = int(input("  ¿Entre cuántas personas? "))

        resultado = dividir_cuenta(total, personas)

        if isinstance(resultado, str):
            print(f"  {resultado}")
        else:
            print(f"\n  Total    : Q{total:.2f}")
            print(f"  Personas : {personas}")
            print(f"  Cada uno paga: Q{resultado:.2f}")
            historial.append(f"Cuenta Q{total:.2f} dividida entre {personas} → Q{resultado:.2f} c/u")

    except ValueError:
        print("  Error: ingresa solo números.")

def opcion_descuento_propina():
    try:
        subtotal     = float(input("\n  Ingresa el subtotal: Q"))
        descuento    = float(input("  Porcentaje de descuento: "))
        porcentaje   = float(input("  Porcentaje de propina (sugerido 10/15/20): "))

        sub_descontado = aplicar_descuento(subtotal, descuento)
        propina        = calcular_propina(sub_descontado, porcentaje)
        total          = calcular_total(sub_descontado, propina)

        print(f"\n  Subtotal original : Q{subtotal:.2f}")
        print(f"  Descuento {descuento}%    : -Q{subtotal - sub_descontado:.2f}")
        print(f"  Subtotal ajustado : Q{sub_descontado:.2f}")
        print(f"  Propina {porcentaje}%     : Q{propina:.2f}")
        print(f"  Total a pagar     : Q{total:.2f}")

        historial.append(f"Descuento {descuento}% + propina {porcentaje}% sobre Q{subtotal:.2f} → Total Q{total:.2f}")

    except ValueError:
        print("  Error: ingresa solo números.")

def opcion_resumen():
    print("\n--- Historial de operaciones ---")
    if not historial:
        print("  No hay operaciones registradas aún.")
    else:
        for i, operacion in enumerate(historial, 1):
            print(f"  {i}. {operacion}")


# --- Función principal ---

def main():
    print("\n  Bienvenido al sistema de cuentas")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción (1-5): ")

        if opcion == "1":
            opcion_propina()
        elif opcion == "2":
            opcion_dividir()
        elif opcion == "3":
            opcion_descuento_propina()
        elif opcion == "4":
            opcion_resumen()
        elif opcion == "5":
            print("\n  ¡Gracias por visitarnos! Hasta pronto.\n")
            break
        else:
            print("  Opción no válida. Elige entre 1 y 5.")

main()