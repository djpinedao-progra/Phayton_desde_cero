# --- Funciones ---

def tabla(n, hasta=10):
    print(f"\n  Tabla del {n}")
    print("  " + "-" * 20)
    for i in range(1, hasta + 1):
        print(f"  {n} x {i:>2} = {n * i:>3}")
    print("  " + "-" * 20)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tablas_primos(limite, hasta=10):
    primos = []
    for n in range(2, limite + 1):
        if es_primo(n):
            primos.append(n)

    print("=" * 40)
    print(f"  Tablas de números primos hasta {limite}")
    print(f"  Primos encontrados: {primos}")
    print("=" * 40)

    for primo in primos:
        tabla(primo, hasta)


# --- Programa principal ---

print("=== Generador de Tablas de Multiplicar ===")
print("1. Tabla de un número")
print("2. Tablas de números primos")

opcion = input("\nElige una opción (1/2): ")

if opcion == "1":
    n     = int(input("¿De qué número quieres la tabla? "))
    hasta = int(input("¿Hasta qué número? (Enter para 10): ") or 10)
    tabla(n, hasta)

elif opcion == "2":
    limite = int(input("¿Hasta qué límite buscar primos? "))
    hasta  = int(input("¿Cada tabla hasta qué número? (Enter para 10): ") or 10)
    tablas_primos(limite, hasta)

else:
    print("Opción no válida.")