# Pedimos al usuario que ingrese un carácter
caracter = input("Ingrese caracter: ")

# Verificamos si el carácter es un número
if caracter.isdigit():
    print("Es numero.")
# Verificamos si el carácter es una letra
elif caracter.isalpha():
    # Si es mayúscula
    if caracter.isupper():
        print("Es letra mayúscula.")
    # Si es minúscula
    else:
        print("Es letra minúscula.")
# Si no es ni letra ni número
else:
    print("No es letra ni número.")
