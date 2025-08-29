# 2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, 
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la 
# función. 

def operaciones(num1:int, num2:int):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    print(f"La suma de {num1} y {num2} es {suma}")
    print(f"La resta de {num1} y {num2} es {resta}")
    print(f"La multiplicacion de {num1} y {num2} es {multiplicacion}")

numero1 = int(input("Diga un numero\n- - ->: "))
print()
numero2 = int(input("Diga otro numero\n- - ->: "))

operaciones(numero1, numero2)