# Solución 8 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    numero = int(input("Ingrese un entero positivo: "))
    if numero < 1:
        print("Debe ingresar un número mayor o igual a 1.")
    else:
        for valor in range(numero, 0, -1):
            print(valor)
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
