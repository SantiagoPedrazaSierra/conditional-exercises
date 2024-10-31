def tipo_triangulo(a, b, c):
    # Verificar si el triángulo es válido
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido."
    
    # Determinar el tipo de triángulo
    if a == b == c:
        return "El triángulo es equilátero."
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."

# Solicitar lados del triángulo al usuario
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Llamar a la función y mostrar el resultado
resultado = tipo_triangulo(a, b, c)
print(resultado)
