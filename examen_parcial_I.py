# 1. Pedir el total de la cuenta
total_cuenta = float(input("Introduce el total de la cuenta: "))

# 2. Pedir el porcentaje de propina
porcentaje = int(input("Introduce el porcentaje de propina (10, 15 o 20): "))

# 3. Validar el porcentaje y realizar cálculos
if porcentaje == 10 or porcentaje == 15 or porcentaje == 20:
    # Calcular la propina
    monto_propina = total_cuenta * (porcentaje / 100)
    
    # Calcular el total final
    total_con_propina = total_cuenta + monto_propina
    
    # 4. Mostrar resultados usando F-strings
    print(f"\n--- Resumen de la cuenta ---")
    print(f"Propina ({porcentaje}%): ${monto_propina:.2f}")
    print(f"Total a pagar: ${total_con_propina:.2f}")

else:
    print("Porcentaje no válido. Por favor, elige entre 10, 15 o 20.")