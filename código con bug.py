# Programa para validar si una persona es mayor de edad
# Contiene un BUG intencional para que lo identifiques

edad = input("Ingresa tu edad: ")

# Agregar prints para investigar
print(f"DEBUG tipo: {type(edad)}")
print(f"DEBUG valor: [{edad}]")
print(f"DEBUG len: {len(edad)}")

if edad >= 18:  # Bug aquí!
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
