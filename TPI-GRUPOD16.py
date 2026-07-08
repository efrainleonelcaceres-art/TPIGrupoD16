MAX_TURNOS_DIARIOS = 4

totalPacientes = 0
totalAtendidos = 0
totalUrgentes = 0

sala_de_espera = []

paciente_en_consulta = "Ninguno (Consultorio Libre)"

def validar_rango(valor: int, minimo: int, maximo: int) -> bool:
    """Función condicional que verifica si un número está dentro de los límites."""
    return minimo <= valor <= maximo


def leer_y_validar_entero(mensaje_ingreso: str, minimo: int, maximo: int, mensaje_error: str) -> int:
    """Procedimiento iterativo para la lectura segura de enteros y control de excepciones."""
    while True:
        try:
            valor = int(input(mensaje_ingreso))
            if validar_rango(valor, minimo, maximo):
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido (Ej: un número sin letras).")


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

def atender_siguiente():
    global totalAtendidos, sala_de_espera, paciente_en_consulta
    
    if len(sala_de_espera) > 0:
        totalAtendidos += 1  
        
        paciente_actual = sala_de_espera.pop(0)
        
        paciente_en_consulta = f"{paciente_actual['nombre']} (Turno: {paciente_actual['turno_nro']} - Especialidad: {paciente_actual['especialidad']})"
        
        print("\n" + "="*40)
        print("¡PACIENTE INGRESADO A CONSULTA EXITOSAMENTE!")
        print("="*40)
        print(f"Paciente: {paciente_actual['nombre']}")
        print(f"DNI: {paciente_actual['dni']}")
        print(f"Especialidad: {paciente_actual['especialidad']}")
        print(f"Prioridad de Atención: {paciente_actual['prioridad']}")
        print("-"*40)
        print(f"Pacientes restantes en sala de espera: {len(sala_de_espera)}")
    else:
        print("\nError: No hay ningún paciente registrado en espera de atención.")

def mostrar_estadisticas():
    global sala_de_espera, paciente_en_consulta
    
    print("\n=== REPORTE ESTADÍSTICO DIARIO ===")
    print(f"Total de turnos otorgados en el día: {totalPacientes} de {MAX_TURNOS_DIARIOS}")
    print(f"Total de pacientes ya atendidos: {totalAtendidos}")
    print(f"Total de casos críticos/urgentes registrados: {totalUrgentes}")
    print("-"*40)
    
    print(f"Paciente actualmente EN CONSULTA: {paciente_en_consulta}")
    print(f"Cantidad de pacientes EN ESPERA: {len(sala_de_espera)}")
    
    if len(sala_de_espera) > 0:
        print("\nLista de personas en espera (por orden de llegada):")
        for p in sala_de_espera:
            print(f" -> Turno Nro {p['turno_nro']}: {p['nombre']} [{p['especialidad']}]")

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