# Script para modelar un estudiante y calcular su promedio

class Estudiante:
    """Clase que representa a un estudiante."""

    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []  # Lista vacía al inicio

    def agregar_nota(self, nota):
        """Añade una nota a la lista de notas."""
        self.notas.append(nota)

    def promedio(self):
        """Retorna el promedio de notas, o 0 si no hay notas."""
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        """Retorna True si el promedio es >= 61."""
        return self.promedio() >= 61


# Solicitar datos del estudiante
nombre = input("Ingrese el nombre: ")
carnet = input("Ingrese el carné: ")
carrera = input("Ingrese la carrera: ")

estudiante = Estudiante(nombre, carnet, carrera)

# Solicitar notas
cantidad = int(input("¿Cuántas notas?: "))
for i in range(cantidad):
    nota = float(input(f"Nota {i + 1}: "))
    estudiante.agregar_nota(nota)

# Mostrar resultados
print(f"\nNombre: {estudiante.nombre}")
print(f"Carné: {estudiante.carnet}")
print(f"Carrera: {estudiante.carrera}")
print(f"Promedio: {estudiante.promedio():.2f}")
print(f"Aprobado: {'Sí' if estudiante.aprobado() else 'No'}")