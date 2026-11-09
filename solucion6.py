# Solución 6 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    numero = int(input("Número para la tabla: "))
    for factor in range(1, 11):
        print(f"{numero} x {factor} = {numero * factor}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
