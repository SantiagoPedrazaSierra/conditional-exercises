from time import localtime

# Obtener la fecha actual
t = localtime()
dia_actual = t.tm_mday
mes_actual = t.tm_mon
anio_actual = t.tm_year

# Solicitar la fecha de nacimiento al usuario
dia_nacimiento = int(input("Ingrese su fecha de nacimiento.\nDía: "))
mes_nacimiento = int(input("Mes: "))
anio_nacimiento = int(input("Año: "))

# Calcular la edad
edad = anio_actual - anio_nacimiento

# Ajustar la edad si el cumpleaños aún no ha ocurrido este año
if (mes_nacimiento > mes_actual) or (mes_nacimiento == mes_actual and dia_nacimiento > dia_actual):
    edad -= 1

# Mostrar la edad
print(f"\nUsted tiene {edad} años.")