# Solución 2 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # Comparar longitudes; informar también los empates.
    textos = []
    for numero in range(1, 4):
        textos.append(input(f"Ingrese el texto {numero}: "))
    mayor = max(len(texto) for texto in textos)
    for numero, texto in enumerate(textos, start=1):
        if len(texto) == mayor:
            print(f"Texto {numero}: {texto!r}, con {mayor} caracteres (longitud máxima).")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
