# 7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si 
# es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la 
# edad al usuario y mostrar un mensaje apropiado. 

def verificar_edad(edad:int)->bool:
    acceso = True
    if edad >= 18:
        acceso = True
    else:
        acceso = False

    return acceso

años = int(input("Que edad tenes?\n- - ->: "))

if verificar_edad(años) == True:
    print("Usted es mayor de edad")
else:
    print("No es mayor de edad.")