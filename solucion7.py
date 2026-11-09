# Solución 7 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    cantidad = int(input("¿Cuántos números desea promediar? "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
    else:
        suma = 0
        for posicion in range(1, cantidad + 1):
            numero = float(input(f"Número {posicion}: "))
            suma += numero
        print(f"Promedio: {suma / cantidad:g}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
