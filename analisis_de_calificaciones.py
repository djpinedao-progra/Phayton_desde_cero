# --- Funciones auxiliares ---

def promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def mayor(notas):
    mayor_nota = notas[0]
    for nota in notas:
        if nota > mayor_nota:
            mayor_nota = nota
    return mayor_nota

def menor(notas):
    menor_nota = notas[0]
    for nota in notas:
        if nota < menor_nota:
            menor_nota = nota
    return menor_nota

def contar_aprobados(notas, minimo=61):
    aprobados = 0
    for nota in notas:
        if nota >= minimo:
            aprobados += 1
    return aprobados

def histograma(notas):
    print("\n--- Histograma ---")
    for nota in notas:
        barras = "*" * (nota // 10)
        print(f"  {nota:>3}: {barras}")

# --- Reporte completo ---

def reporte(notas):
    aprobados  = contar_aprobados(notas)
    reprobados = len(notas) - aprobados

    print("=" * 40)
    print("       REPORTE DE NOTAS")
    print("=" * 40)
    print(f"  Total de estudiantes : {len(notas)}")
    print(f"  Promedio             : {promedio(notas):.2f}")
    print(f"  Nota más alta        : {mayor(notas)}")
    print(f"  Nota más baja        : {menor(notas)}")
    print(f"  Aprobados  (>= 61)   : {aprobados}")
    print(f"  Reprobados (< 61)    : {reprobados}")
    print("=" * 40)
    histograma(notas)


# --- Programa principal ---

notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
reporte(notas)