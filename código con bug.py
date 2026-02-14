# Programa para validar si una persona es mayor de edad
# Contiene un BUG intencional para que lo identifiques

edad = int (input("Ingresa tu edad: "))

# Agregar prints para investigar
print(f"DEBUG tipo: {type(edad)}")
print(f"DEBUG valor: {edad}")

if edad >= 18:  # Bug arreglado!
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
