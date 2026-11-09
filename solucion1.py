# Solución 1 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # Descuento de un producto. Se usan límites estrictos: precio < límite.
    precio = float(input("Precio del producto: Q"))
    if precio < 0:
        print("El precio no puede ser negativo.")
    else:
        if precio < 100:
            porcentaje = 5
        elif precio < 200:
            porcentaje = 10
        elif precio < 500:
            porcentaje = 15
        elif precio < 800:
            porcentaje = 20
        else:
            porcentaje = 25
        descuento = precio * porcentaje / 100
        print(f"Descuento ({porcentaje}%): Q{descuento:.2f}")
        print(f"Precio final: Q{precio - descuento:.2f}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
