#Calculadoras de números enteros en Python

#Sumas de dos números enteros en Python

print("Esto es una suma de dos números enteros")
print()

primerNumero = input("Ingrese el primer número entero: ")

if primerNumero.isnumeric():
    primerNumero = int(primerNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()


segundoNumero = input("Ingrese el segundo número entero: ")
print()

if segundoNumero.isnumeric():
    segundoNumero = int(segundoNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()

resultado = primerNumero + segundoNumero
print("El resultado de la suma es:", resultado)
print()
print("--------------------------------------------------")
print()


#Resta de dos números enteros en Python

print("Esto es una resta de dos números enteros")
print()

primerNumero = input("Ingrese el primer número entero: ")

if primerNumero.isnumeric():
    primerNumero = int(primerNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()


segundoNumero = input("Ingrese el segundo número entero: ")
print()

if segundoNumero.isnumeric():
    segundoNumero = int(segundoNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()

resultado = primerNumero - segundoNumero
print("El resultado de la resta es:", resultado)
print()
print("--------------------------------------------------")
print()

#Multiplicacion de dos números enteros en Python

print("Esto es una multiplicación de dos números enteros")
print()

primerNumero = input("Ingrese el primer número entero: ")

if primerNumero.isnumeric():
    primerNumero = int(primerNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()


segundoNumero = input("Ingrese el segundo número entero: ")
print()

if segundoNumero.isnumeric():
    segundoNumero = int(segundoNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()

resultado = primerNumero * segundoNumero
print("El resultado de la multiplicación es:", resultado)
print()
print("--------------------------------------------------")
print()

#División de dos números enteros en Python

print("Esto es una división de dos números enteros")
print()

primerNumero = input("Ingrese el primer número entero: ")

if primerNumero.isnumeric():
    primerNumero = int(primerNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()


segundoNumero = input("Ingrese el segundo número entero: ")
print()

if segundoNumero.isnumeric():
    segundoNumero = int(segundoNumero)
else:
    print("El valor ingresado no es un número entero.")
    exit()

resultado = primerNumero / segundoNumero
print("El resultado de la división es:", resultado)
print()
print("--------------------------------------------------")
print()

print("Fin del programa.")
