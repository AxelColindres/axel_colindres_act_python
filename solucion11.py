# Solución 11 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    palabra = input("Ingrese una palabra: ")
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
    print(f"Palabra al revés: {invertida}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
