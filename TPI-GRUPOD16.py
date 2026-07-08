MAX_TURNOS_DIARIOS = 4

totalPacientes = 0
totalAtendidos = 0
totalUrgentes = 0

sala_de_espera = []

paciente_en_consulta = "Ninguno (Consultorio Libre)"

def registrar_nuevo_paciente():
    """Módulo encargado de validar el cupo diario general y registrar un paciente en la lista."""
    global totalPacientes, totalUrgentes, sala_de_espera
    
    if totalPacientes == MAX_TURNOS_DIARIOS:
        print(f"\nALERTA: No se pueden emitir más turnos. Se alcanzó el cupo máximo diario de {MAX_TURNOS_DIARIOS}.")
        return 

    totalPacientes += 1
    
    print(f"\n=== REGISTRO DE PACIENTE (Turno Nro: {totalPacientes}) ===")
    
    dni = leer_y_validar_entero(
        "Ingrese el DNI del paciente (8 dígitos): ", 
        1000000, 99999999, 
        "Error: DNI inválido. Debe tener entre 7 y 8 dígitos numéricos."
    )
    
    nombre_completo = input("Ingrese Apellido y Nombres: ")
    
    print("\n--- Seleccione la Especialidad Médica ---")
    print("1. Clínica Médica")
    print("2. Pediatría")
    print("3. Cardiología")
    print("4. Traumatología")
    print("5. Ginecología")
    
    opcion_especialidad = leer_y_validar_entero(
        "Seleccione una opción (1-5): ", 
        1, 5, 
        "Error: Opción incorrecta. Ingrese un número del 1 al 5."
    )
    
    match opcion_especialidad:
        case 1: especialidad = "Clínica Médica"
        case 2: especialidad = "Pediatría"
        case 3: especialidad = "Cardiología"
        case 4: especialidad = "Traumatología"
        case 5: especialidad = "Ginecología"
    
    prioridad = leer_y_validar_entero(
        "\nSeleccione Prioridad (1: Urgente / 2: Media / 3: Baja): ", 
        1, 3, 
        "Error: Prioridad incorrecta. Ingrese un valor válido (1, 2 o 3)."
    )

    if prioridad == 1:
        totalUrgentes += 1

    nuevo_paciente = {
        "turno_nro": totalPacientes,
        "dni": dni,
        "nombre": nombre_completo,
        "especialidad": especialidad,
        "prioridad": prioridad
    }
    
    sala_de_espera.append(nuevo_paciente)

    print(f"\n¡Turno de {nombre_completo} registrado exitosamente!")
    print(f"Especialidad asignada: {especialidad}")
    print(f"Pacientes actualmente en sala de espera: {len(sala_de_espera)}")
    print(f"Turnos disponibles restantes para hoy: {MAX_TURNOS_DIARIOS - totalPacientes}")


def main():
    while True: 
        print("\n" + "-"*40)
        print("=== SISTEMA DE GESTIÓN DE TURNOS ===")
        print("1. Registrar paciente")
        print("2. Atender próximo paciente")
        print("3. Mostrar estadísticas")
        print("4. Salir")
        print("-"*40)
        
        opcion = leer_y_validar_entero(
            "Seleccione una opción (1-4): ", 
            1, 4, 
            "Opción inválida. Por favor, seleccione un número válido del menú (1 al 4)."
        )

        match opcion:
            case 1:
                registrar_nuevo_paciente()
            case 2:
                atender_siguiente()
            case 3:
                mostrar_estadisticas()
            case 4:
                print("\nCierre de jornada médica. Liberando memoria del sistema.")
                break 


if __name__ == "__main__":
    main()