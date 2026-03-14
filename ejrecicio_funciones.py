def area_circulo(radio):
    pi = 3.1416
    area = pi * radio ** 2
    return area
    

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def celsius_a_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def maximo(lista):
    if not lista:
        return None
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

print(f'("Estos son los valores del área de un círculo con diferentes radios")')
print(area_circulo(5))  # Ejemplo de uno
print(area_circulo(10)) # Ejemplo de dos
print(area_circulo(2.5)) # Ejemplo de tres

print(f'("Estos son los numeros primos")')
print(es_primo(1)) 
print(es_primo(5))
print(es_primo(10))

print(f'("Estos son los factoriales")')
print(factorial(5))
print(factorial(0))
print(factorial(7))

print(f'("Estos son los números de Fibonacci")')
print(fibonacci(10))
print(fibonacci(0))
print(fibonacci(1))

print(f'("Estos son los valores de Celsius a Fahrenheit")')
print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(0))
print(celsius_a_fahrenheit(37))

print(f'("Estos son los valores máximos de una lista")')
print(maximo([3, 1, 4, 1, 5, 9]))
print(maximo([-1, -5, -3]))
print(maximo([]))

