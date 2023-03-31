import random

# Pedir el nombre del usuario
nombre = input("Hola, ¿cuál es tu nombre? ")

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar el número de intentos en 0
intentos = 0

# Jugar hasta que el usuario adivine el número o se agoten los intentos
while intentos < 8:
    # Pedir al usuario que adivine el número
    adivinanza = int(input("Bueno, " + nombre + ", he pensado un número entre 1 y 100. ¿Cuál crees que es? "))

    # Validar si el número elegido está permitido
    if adivinanza < 1 or adivinanza > 100:
        print("El número que has elegido no está permitido. Por favor, elige un número entre 1 y 100.")
        continue

    # Incrementar el número de intentos
    intentos += 1

    # Validar si el usuario ha acertado
    if adivinanza == numero_secreto:
        print("¡Felicidades, " + nombre + "! Has ganado en", intentos, "intentos.")
        break

    # Informar si el número es mayor o menor al número secreto
    if adivinanza < numero_secreto:
        print("Tu respuesta es incorrecta. Has elegido un número menor al número secreto. Intenta de nuevo.")
    else:
        print("Tu respuesta es incorrecta. Has elegido un número mayor al número secreto. Intenta de nuevo.")

# Si se han agotado los intentos y el usuario no ha acertado, informar que ha perdido
if intentos == 8:
    print("Lo siento, " + nombre + ". Has perdido. El número secreto era", numero_secreto, ".")
