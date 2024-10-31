#Entrada de Datos

a= int(input("Juegos ganados por A: "))
b= int(input("Juegos ganados por B: "))

#Verificar condiciones de victoria
if a > 7 or b > 7 or (a == 7 and b < 5) or (b == 7 and a <5):
    print("Invalido")
if (a == 6 and b <= 4) or (a == 7 and (b == 5 or b == 6)):
    print("Gano A")
elif (b == 6 and a <= 4) or (b == 7 and (a == 5 or a == 6)):
    print ("Gano B")

#Verificacion de set en curso
else:
    print ("Aun no termina")
         
