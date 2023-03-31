import random

# Lista de palabras a elegir
palabras = ["python", "programacion", "telefono", "algoritmo", "computadora"]

# Elegir una palabra al azar
palabra_secreta = random.choice(palabras)

# Inicializar las variables
vidas = 6
adivinadas = []
for letra in palabra_secreta:
    adivinadas.append("_")

# Función para imprimir el estado del juego
def imprimir_juego():
    print("Vidas restantes:", vidas)
    print(" ".join(adivinadas))

# Bucle principal del juego
while vidas > 0:
    imprimir_juego()
    letra = input("Ingresa una letra: ")
    if letra in palabra_secreta:
        # Actualizar las letras adivinadas
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                adivinadas[i] = letra
        print("¡Correcto!")
    else:
        # Restar una vida
        vidas -= 1
        print("¡Incorrecto!")
    if "".join(adivinadas) == palabra_secreta:
        # El jugador ha adivinado la palabra
        print("¡Ganaste!")
        break

# Si se llega aquí, el jugador ha perdido
if vidas == 0:
    print("Perdiste. La palabra era:", palabra_secreta)
