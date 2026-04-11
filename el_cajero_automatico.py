# Cajero Automático
def calcular_billetes(monto):
    if monto % 5 != 0:
        print("Error: el monto debe ser múltiplo de 5.")
        return None
    
    denominaciones = [200, 100, 50, 20, 10, 5]
    billetes = {}
    
    for billete in denominaciones:
        billetes[billete] = monto // billete
        monto %= billete
    
    return billetes


# --- Programa principal ---
monto = int(input("Ingresa el monto en quetzales: "))
resultado = calcular_billetes(monto)

if resultado is not None:
    print(f"\nBilletes necesarios para Q{monto}:")
    for denominacion, cantidad in resultado.items():
        print(f"  Q{denominacion}: {cantidad} billete(s)")
