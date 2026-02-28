import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

while intentos < max_intentos:
    intento = int(input("Adivina (1-100): "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo")
    elif intento > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"¡Correcto! en "
                f"{intentos} intentos.")
        break

if intentos == max_intentos and intento != numero_secreto:
    print(f"¡Perdiste! El número era {numero_secreto}")
