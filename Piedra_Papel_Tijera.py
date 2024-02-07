# Juego de piedra, papel o tijera.

# Importación del módulo random para generar opciones aleatorias.
import random

# Definición de las opciones disponibles para el juego.
options = ("piedra", "papel", "tijera")

# Definición de las reglas del juego, usando un diccionario que asocia cada opción con la que le gana.
rules = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

# Inicialización del contador de victorias de la computadora.
computer_wins = 0

# Inicialización del contador de victorias del usuario.
user_wins = 0

# Inicialización del contador de rondas.
rounds = 1

# Bucle principal del juego.
while True:
    # Muestra el encabezado de la ronda.
    print("*" * 30)
    print(f"ROUND {rounds}") # Uso de f-strings para formatear el texto con variables.
    print("*" * 30)

    # Muestra el número de victorias de la computadora y el usuario.
    print(f"Computer_wins {computer_wins}")
    print(f"User_wins {user_wins}")

    try:
        # Solicita al usuario que elija una opción.
        user_option = input("Eliga una: piedra, papel o tijera: ")

        # Convierte la entrada del usuario a minúsculas para simplificar la comparación.
        user_option = user_option.lower()

        # Verifica si la opción elegida por el usuario no está en las opciones válidas.
        if user_option not in options:
            raise ValueError("Opción inválida. Por favor, elija entre piedra, papel o tijera.")

        # Incrementa el contador de rondas.
        rounds += 1

        # Genera una opción aleatoria para la computadora.
        computer_option = random.choice(options)

        # Muestra las opciones elegidas por el usuario y la computadora.
        print(f"User option: {user_option}")
        print(f"Computer option: {computer_option}")

        # Evaluación de los resultados de la ronda.
        if user_option == computer_option:
            print("Empate.")
        elif rules[user_option] == computer_option: # Uso del diccionario de reglas para simplificar la lógica.
            print(f"{user_option.capitalize()} gana a {computer_option}.") # Uso de capitalize() para poner la primera letra en mayúscula.
            print("¡El usuario ganó!")
            user_wins += 1
        else:
            print(f"{computer_option.capitalize()} gana a {user_option}.")
            print("¡La computadora ganó!")
            computer_wins += 1

        # Verifica si la computadora o el usuario han ganado dos veces, usando el operador lógico or.
        if computer_wins == 2 or user_wins == 2:
            print(f"El ganador es {'la computadora' if computer_wins > user_wins else 'el usuario'}.") # Uso de una expresión condicional para determinar el ganador.
            break

    except ValueError as e:
        print(e)  # Imprime el mensaje de error
