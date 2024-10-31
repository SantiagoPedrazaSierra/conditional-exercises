# Pedimos al usuario que ingrese un año
año = int(input("Ingrese un año: "))

# Determinamos si el año es bisiesto según el calendario vigente
if año >= 1582:  # Calendario gregoriano
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
else:  # Calendario juliano
    if año % 4 == 0:
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")

