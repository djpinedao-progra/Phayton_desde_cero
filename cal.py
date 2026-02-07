print("Bienvenido a la calculadora")
print("Por favor ingresa los datos y luego escoge la operación")

num_1 = int (input ("Ingrese el primer numeor"))

num_2 = int (input("Ingrese el segundo numero"))

ope = input ("ingresa la opreción que quieres realizar") 
print("Suma: +")
print("Resta: -")
print("Multiplicación: *")
print("División: /")
print("Ingrese el simbolo de la opración a realizar")

match ope:
    case "+":
        print(num_1+num_2)
    case "-":
        print(num_1-num_2)
    case "*":
        print(num_1*num_2)
    case "/":
        print(num_1/num_2)
    case _:
      print("Operación no válida")




