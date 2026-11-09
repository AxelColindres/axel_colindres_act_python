# Solución 16 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    cantidad = 0
    nombre = input("Nombre del estudiante (fin para terminar): ").strip()
    while nombre.lower() != "fin":
        if nombre:
            cantidad += 1
            print(f"Estudiante {cantidad}: {nombre}")
        else:
            print("El nombre no puede estar vacío.")
        nombre = input("Nombre del estudiante (fin para terminar): ").strip()
    print(f"Total de estudiantes ingresados: {cantidad}")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
