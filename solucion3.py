# Solución 3 - Didáctica de la programación
# Axel Colindres | USAC - EFPEM

try:
    # La alerta de seguridad tiene prioridad sobre las demás condiciones.
    tipo = input("Tipo de usuario (estudiante/instructor): ").strip().lower()
    credencial = input("¿Credencial activa? (si/no): ").strip().lower()
    hora = float(input("Hora actual en formato decimal de 0 a menos de 24: "))
    alerta = input("¿Existe alerta de seguridad? (si/no): ").strip().lower()
    respuestas = ("si", "sí", "no")
    if credencial not in respuestas or alerta not in respuestas:
        print("Acceso denegado: responda si o no.")
    elif not 0 <= hora < 24:
        print("Acceso denegado: hora inválida.")
    elif alerta in ("si", "sí"):
        print("Acceso denegado: existe una alerta de seguridad.")
    elif credencial == "no":
        print("Acceso denegado: la credencial no está activa.")
    elif tipo == "estudiante":
        if 7 <= hora <= 18:
            print("Acceso permitido al estudiante.")
        else:
            print("Acceso denegado: horario de estudiantes de 7 a 18 horas.")
    elif tipo == "instructor":
        if 6 <= hora <= 21:
            print("Acceso permitido al instructor.")
        else:
            print("Acceso denegado: horario de instructores de 6 a 21 horas.")
    else:
        print("Acceso denegado: tipo de usuario no reconocido.")
except ValueError:
    print("Entrada inválida. Ejecute nuevamente e ingrese el tipo de dato solicitado.")
