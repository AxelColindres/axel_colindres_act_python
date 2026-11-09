# Solución 5 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    import math

    numero1 = float(input("Primer número: "))
    numero2 = float(input("Segundo número: "))
    numero3 = float(input("Tercer número: "))
    suma = numero1 + numero2 + numero3
    print(f"Suma: {suma:g}")
    if suma >= 0:
        print(f"Raíz cuadrada: {math.sqrt(suma):g}")
    else:
        print("La suma negativa no tiene raíz cuadrada real.")
    # Se considera múltiplo de 5 si es un múltiplo entero.
    if suma % 5 == 0:
        print("La suma es múltiplo de 5.")
    else:
        print("La suma no es múltiplo de 5.")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
