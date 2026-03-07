# Tabla de multiplicar - Todas las tablas del 1 al 12
# Bucle anidado

for num in range(1, 13):
    print(f"\n--- Tabla del {num} ---")
    for i in range(1, 13):
        resultado = num * i
        print(f"{num} x {i:2d} = {resultado:3d}")
