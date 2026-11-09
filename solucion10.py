# Solución 10 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    texto = input("Ingrese un texto: ")
    contador = 0
    for letra in texto.lower():
        if letra in "aeiouáéíóúü":
            contador += 1
    print(f"Cantidad de vocales: {contador}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
