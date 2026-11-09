# Solución 12 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # Contraseña establecida antes de iniciar el ciclo, según la actividad.
    contrasena_correcta = "efpemusac2026"
    contrasena = input("Ingrese la contraseña: ")
    while contrasena != contrasena_correcta:
        print("Contraseña incorrecta. Intente nuevamente.")
        contrasena = input("Ingrese la contraseña: ")
    print("Contraseña correcta. Acceso permitido.")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
