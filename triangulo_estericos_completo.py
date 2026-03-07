#Triángulo de asteriscos 
n = 5

#Triángulo centrado
for i in range(1, n + 1):
    espacios = " " * (n - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

#Triángulo centrado
for i in range(n-1, 0, -1):
    espacios = " " * (n - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)