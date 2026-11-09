# Solución 4 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    texto = input("Ingrese un texto: ")
    if texto:
        if texto[0] == texto[-1]:
            print("El primer y el último carácter son iguales.")
        else:
            print("El primer y el último carácter son diferentes.")
    else:
        print("El texto vacío no tiene primer ni último carácter.")
    if len(texto) % 2 == 0:
        print(f"La longitud ({len(texto)}) es par.")
    else:
        print(f"La longitud ({len(texto)}) es impar.")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
