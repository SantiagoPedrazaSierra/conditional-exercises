#Definir cada operador
"""
(+) suma
(-)resta
(*)multiplicacion
(/)division
(**)potencia
"""
#Pedir a usuario que ingrese numeros y operador 
num1=float(input("Operando: "))
op=input("Operador: ")
num2=float(input("Operando: "))

#Operacion de numeros y operadores
def calculadora(num1,num2,op):
    if op == "+":
        print(f" {int(num1)} + {int(num2)} =  {int(num1 + num2)}")
    elif op == "-":
        print(f" {int(num1)} - {int(num2)} =  {int(num1 - num2)}")

    elif op == "*":
        print(f" {int(num1)} * {int(num2)} = {int(num1 * num2)}")
    elif op == "/":
        if num2 != 0: #Verificacion de division por cero
            print(f" {int(num1)} / {int(num2)} = {(num1 / num2)}")
        else:
            print("Error:Division por cero")
    elif op == "**":
        print(f" {int(num1)} ** {int(num2)} = {int(num1 ** num2)}")


#Mostrar resultado
calculadora (num1,num2,op)   
