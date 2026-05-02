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