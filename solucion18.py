# Solución 18 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # Conversión manual: multiplicar el acumulado por 2 y sumar cada dígito.
    binario = input("Ingrese un número binario no negativo: ").strip()
    if not binario or any(digito not in "01" for digito in binario):
        print("Número binario inválido. Utilice únicamente 0 y 1.")
    else:
        decimal = 0
        for digito in binario:
            decimal = decimal * 2 + int(digito)
        print(f"Equivalente decimal: {decimal}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
