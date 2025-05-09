def esPrimo(numero): 
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

numero_ingresado = int(input("Ingrese un numero: "))

if esPrimo(numero_ingresado):
    print("Este es un numero primo")
else:
    print("Este no es un numero primo")