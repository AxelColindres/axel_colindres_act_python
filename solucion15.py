# Solución 15 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    numero = int(input("Ingrese un entero no negativo: "))
    if numero < 0:
        print("El factorial no está definido para enteros negativos.")
    else:
        factorial = 1
        for factor in range(1, numero + 1):
            factorial *= factor
        print(f"{numero}! = {factorial}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
