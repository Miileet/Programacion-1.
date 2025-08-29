# 1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
# un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.



def saludar(nombre:str):
    print(f"Hola {nombre}!")

nombre = input("Cual es su nombre?\n- - ->: ")
saludar(nombre)