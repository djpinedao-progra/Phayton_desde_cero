coordenadas_Esc = (14.3050, -90.7850)
print(coordenadas_Esc,"\n")

lat, lon = coordenadas_Esc

print("Latitud:", lat)
print("Longitud:", lon,"\n")


numeros = [10, 25, 7, 42, 18, 3]

def calcular_estadisticas(lista):
 maximo = max(lista)
 minimo = min(lista)
 promedio = sum(lista) / len(lista)
 return (maximo, minimo, promedio)

resultado = calcular_estadisticas(numeros)
print(resultado)

