#Triángulo de asteriscos 
n = 5
for i in range(1, n + 1):
    print("*" * i)

#Triángulo invertido 
for i in range(n, 0, -1):
    print("*" * i)

#Triángulo centrado
for i in range(1, n + 1):
    espacios = " " * (n - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
