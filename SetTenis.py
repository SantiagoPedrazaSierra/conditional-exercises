def estado_set(juegos_A, juegos_B):
    # Verificar si el resultado es inválido
    if (juegos_A >= 7 and juegos_B > juegos_A) or (juegos_B >= 7 and juegos_A > juegos_B):
        return "Invalido"
    if juegos_A > 6 and juegos_B > 6:
        return "Invalido"
    
    # Verificar si un jugador ha ganado el set
    if juegos_A >= 6 and juegos_A - juegos_B >= 2:
        return "Gano A"
    if juegos_B >= 6 and juegos_B - juegos_A >= 2:
        return "Gano B"

    # Si no hay ganador, verificar si el set está en curso
    return "Aun no termina"

# Solicitar juegos ganados por A y B
while True:
    juegos_A = int(input("Juegos ganados por A: "))
    juegos_B = int(input("Juegos ganados por B: "))
    
    # Llamar a la función y mostrar el resultado
    resultado = estado_set(juegos_A, juegos_B)
    print(resultado)
