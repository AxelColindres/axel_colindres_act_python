# Solución 17 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # El número secreto es fijo, como permite la guía.
    numero_secreto = 25
    intentos = 0
    while True:
        numero = int(input("Adivine el número secreto (entre 1 y 100): "))
        intentos += 1
        if numero > numero_secreto:
            print("El valor ingresado es mayor que el número secreto.")
        elif numero < numero_secreto:
            print("El valor ingresado es menor que el número secreto.")
        else:
            print(f"¡Ganó! Adivinó el número secreto en {intentos} intentos.")
            break
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
