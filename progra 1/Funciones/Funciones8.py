# 8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y 
# devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el 
# año de nacimiento del usuario y mostrar la edad calculada. 

def calcular_edad(año:int)->int:
    año_actual = 2025
    resultado = año - año_actual
    return resultado


edad = int(input("Que edad tenes?\n- - ->: "))
print(calcular_edad(edad))