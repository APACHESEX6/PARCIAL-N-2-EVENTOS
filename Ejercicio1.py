import random

def juego_parcial():
    # Solicitar el rango máximo al usuario
    while True:
        try:
            rango_maximo = int(input("Ingrese el número máximo del rango: "))
            if rango_maximo <= 0:
                raise ValueError("El número máximo debe ser mayor que 0.")
            break
        except ValueError as e:
            print("Error:", e)

    # Calcular el número máximo de intentos (dividir el rango máximo entre 20)
    max_intentos = rango_maximo // 20 if rango_maximo // 20 > 0 else 1  # Asegurarse de que haya al menos un intento
    numero_a_adivinar = random.randint(1, rango_maximo)
    intentos = 0

    # Vector de resultados
    resultados = ["falló"] * (rango_maximo + 1)

    print(f"¡He generado un número entre 1 y {rango_maximo}! Tienes un máximo de {max_intentos} intentos para adivinarlo.")

    while intentos < max_intentos:
        try:
            # Solicitar un número al usuario
            intento = int(input("Intenta adivinar el número: "))
            intentos += 1

            # Comprobar si el número adivinado es correcto
            if intento < 1 or intento > rango_maximo:
                print(f"Por favor, elige un número entre 1 y {rango_maximo}.")
                continue

            if intento == numero_a_adivinar:
                resultados[numero_a_adivinar] = "acertó"
                print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {intentos} intentos.")
                break
            elif intento < numero_a_adivinar:
                print("El número que debes adivinar es mayor.")
            else:
                print("El número que debes adivinar es menor.")
        
        except ValueError:
            print("Error, debes ingresar un número entero.")
            intentos += 1  # Contar como intento fallido

    else:
        print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {numero_a_adivinar}.")

    # Mostrar resultados finales
    print("Resultados de los intentos:", resultados[1:])  # Mostrar solo resultados válidos

# Ejecutar el juego
juego_parcial()

