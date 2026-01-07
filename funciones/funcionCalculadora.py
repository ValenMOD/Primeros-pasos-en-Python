def suma(num1, num2):
    
    resultado = num1 + num2
    return resultado
    
resultadoSuma = suma(5, 4)

print(resultadoSuma)


    
def resta(num1, num2):
    
    resultado = num1 - num2
    return resultado

resultadoResta = resta(9, 2)

print(resultadoResta)


    
def multiplica(num1, num2):
    
    resultado = num1 * num2
    return resultado

resultadoMultiplica = multiplica(3, 2)

print(resultadoMultiplica)



def divide(num1, num2):
    
    resultado = num1 / num2
    resultado = int(resultado) #Esto convierte al resultado de la división en un número entero.
    return resultado
    
resultadoDivide = divide(8, 2)

print(resultadoDivide)
