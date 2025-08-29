# 5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si 
# es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.

def es_par(numero:int)->bool:
    resultado = True
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

numero = int(input("Diga un numero\n- - ->: "))

print(es_par(numero))