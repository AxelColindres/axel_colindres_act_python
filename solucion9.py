# Solución 9 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    numero = int(input("Número para la tabla descendente: "))
    for factor in range(10, 0, -1):
        print(f"{numero} x {factor} = {numero * factor}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
