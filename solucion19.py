# Solución 19 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # Conversión manual mediante divisiones sucesivas entre 2.
    numero = int(input("Ingrese un entero decimal no negativo: "))
    if numero < 0:
        print("Debe ingresar un entero no negativo.")
    else:
        original = numero
        binario = ""
        if numero == 0:
            binario = "0"
        while numero > 0:
            residuo = numero % 2
            binario = str(residuo) + binario
            numero //= 2
        print(f"{original} en binario: {binario}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
