# Solución 13 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    numero = float(input("Ingrese un número (negativo para terminar): "))
    while numero >= 0:
        print(f"Número ingresado: {numero:g}")
        numero = float(input("Ingrese otro número (negativo para terminar): "))
    print("Programa finalizado por ingresar un número negativo.")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
