# Solución 14 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # Se conserva la opción «Python» que aparece literalmente en la guía.
    opcion = ""
    while opcion != "4":
        print("\n1. Python\n2. Resta\n3. Multiplicación\n4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("Python es un lenguaje de programación de sintaxis sencilla.")
        elif opcion == "2":
            numero1 = float(input("Primer número: "))
            numero2 = float(input("Segundo número: "))
            print(f"Resta: {numero1 - numero2:g}")
        elif opcion == "3":
            numero1 = float(input("Primer número: "))
            numero2 = float(input("Segundo número: "))
            print(f"Multiplicación: {numero1 * numero2:g}")
        elif opcion == "4":
            print("Programa finalizado.")
        else:
            print("Opción inválida. Seleccione de 1 a 4.")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
