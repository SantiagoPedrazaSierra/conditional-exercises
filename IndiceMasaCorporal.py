def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def condicion_riesgo(imc, edad):
    if edad < 45:
        if imc < 22.0:
            return "bajo"
        else:
            return "medio"
    else:  # edad ≥ 45
        if imc < 22.0:
            return "medio"
        else:
            return "alto"

# Solicitar datos al usuario
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))
edad = int(input("Ingrese su edad: "))

# Calcular el IMC
imc = calcular_imc(peso, estatura)

# Obtener la condición de riesgo
riesgo = condicion_riesgo(imc, edad)

# Mostrar el resultado
print(f"Su IMC es: {imc:.2f}")
print(f"Condición de riesgo: {riesgo}")
