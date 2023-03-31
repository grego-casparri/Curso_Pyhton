from numeros import turno_perfumeria, turno_farmacia, turno_cosmeticos, mensaje_turno


def seleccionar_area():
    while True:
        area = input("¿A qué área desea dirigirse? (P) Perfumería, (F) Farmacia, (C) Cosméticos: ")
        if area.upper() == 'P':
            return turno_perfumeria()
        elif area.upper() == 'F':
            return turno_farmacia()
        elif area.upper() == 'C':
            return turno_cosmeticos()
        else:
            print("Por favor, seleccione una opción válida.")


@mensaje_turno
def obtener_turno(turnos):
    return next(turnos)


def main():
    turnos = seleccionar_area()
    print(obtener_turno(turnos))

    while True:
        continuar = input("¿Desea sacar otro turno? (S/N): ")
        if continuar.upper() == 'S':
            print(obtener_turno(turnos))
        elif continuar.upper() == 'N':
            print("Gracias por utilizar nuestro servicio de turnos.")
            break
        else:
            print("Por favor, seleccione una opción válida.")


if __name__ == '__main__':
    main()
