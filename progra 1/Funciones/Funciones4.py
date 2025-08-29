# 4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números 
# ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números 
# ordenados. 

def buscar_mayor(num1:int, num2:int, num3:int):
    num_mayor = num1
    num_mayor2 = num3
    chiquito = num2
    if num_mayor < num3 and num3 > num2:
        num_mayor = num3
        if num2 > num1:
            num_mayor2 = num2
            chiquito = num3
        else:
            num_mayor2 = num3
            chiquito = num2

    return num_mayor, num_mayor2, chiquito

numero1 = int(input("Diga un numero\n- - ->: "))
print()
numero2 = int(input("Diga un numero\n- - ->: "))
print()
numero3 = int(input("Diga un numero\n- - ->: "))

print(f"Los numeros ordenados de mayor a menor son: {buscar_mayor(numero1,numero2,numero3)}")




