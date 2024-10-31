# Pedimos al usuario que ingrese dos números
numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))

# Ordenamos e imprimimos
if numero1 < numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)

# Pedimos al usuario que ingrese tres números
numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))
numero3 = int(input("Ingrese numero: "))

# Usamos una lista para ordenar y luego imprimimos
numeros = [numero1, numero2, numero3]
numeros.sort()  # Ordenamos la lista
print(*numeros)  # Mostramos los números ordenados

# Pedimos al usuario que ingrese cuatro números
numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))
numero3 = int(input("Ingrese numero: "))
numero4 = int(input("Ingrese numero: "))

# Usamos una lista para ordenar y luego imprimimos
numeros = [numero1, numero2, numero3, numero4]
numeros.sort()  # Ordenamos la lista
print(*numeros)  # Mostramos los números ordenados
