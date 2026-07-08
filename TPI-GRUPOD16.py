MAX_TURNOS_DIARIOS = 4

totalPacientes = 0
totalAtendidos = 0
totalUrgentes = 0

sala_de_espera = []

paciente_en_consulta = "Ninguno (Consultorio Libre)"

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