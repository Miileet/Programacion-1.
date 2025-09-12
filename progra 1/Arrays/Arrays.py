

def cargar_numeros():
# 1. Cargar y mostrar array: 
# Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un 
# ciclo for. 
    array = [0] * 5

    for i in range(len(array)):
        array[i] = int(input(f"Seleccione el numero que va a haber en la posicion {i+1}: "))
    print(f"Contenido del array: {array}")

def sumar_elementos():
# Sumar todos los elementos: 
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los 
# elementos. 
    array = [0] * 10
    suma = 0
    for i in range(len(array)):
        array[i] = int(input(f"Seleccione el numero que va a haber en la posicion {i+1}: "))

    for j in range(len(array)):
        suma += array[j]
    print(f"La suma de todos los elementos cargados es: {suma}")

def calcular_promedio():
# 3. Promedio de valores: 
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio 
# de los valores. 
    array = [0] * 6
    suma = 0
    for i in range(len(array)):
        array[i] = float(input(f"Seleccione el numero que va a haber en la posicion {i+1}: "))
    for j in range(len(array)):
        suma += array[j]
    promedio = suma / len(array)
    print(f"El promedio de los numeros ingresados es: {promedio}")

def contar_mayores():
# 4. Contar mayores a un valor: 
# Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado. 
    array = [0] * 8
    array_mayor_100 = 0
    for i in range(len(array)):
        array[i] = int(input(f"Seleccione el numero que va a haber en la posicion {i+1}: "))
    for j in range(len(array)):
        if array[j] > 100:
            array_mayor_100 += 1
    print(f"La cantidad de numeros mayores a 100 son: {array_mayor_100}")

def buscar_valor():
# 5. Buscar un valor: 
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array. 
# Informar la posición en caso afirmativo, o indicar que no se encuentra. 
    array = [1,2,3,4,5,6,7,8,9,10]
    numero = int(input("Mencione un numero para verificar si se encuentra en la array\n- - ->: "))
    for i in range(len(array)):
        if numero == array[i]:
            print(f"El numero {array[i]} esta en el array, y se encuentra en la posicion {i+1}")
            break
    else:
        print(f"El numero {numero} no se encuentra en el array")  

def buscar_mayor():
# 6. Mayor y su posición: 
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se 
# encuentra.
    array = [2,4,3,1,7,6,5]
    mayor = array[0]
    posicion = 0
    for i in range(len(array)):
        if array[i] > mayor:
            mayor = array[i]
            posicion = i
    print(f"El valor mas alto dentro del array es {mayor}, que esta en la posocion {posicion}")

def invertir_orden():
# 7. Invertir orden: 
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero. 
    array = [1,2,3,4,5,6]
    for i in range(len(array)-1,-1,-1):
        print(array[i])

def comparar_arrays():
# 8. Comparar dos arrays: 
# Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento 
# y mostrar un mensaje indicando si son o no iguales. 
    array1 = [1,3,5,7,9]
    array2 = [2,5,8,10,1]
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            print("Las arrays no son iguales")
            break
    else:
        print("Las arrays son iguales")

def intercambiar_elementos():
# 9. Intercambiar elementos pares por ceros: 
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array 
# resultante. 
    array = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] = 0
    print(f"Array sin pares: {array}")

def buscar_valor(array:list, numero:int)->int:
# 10. Función para buscar la primera aparición de un valor: 
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar 
# la posición de la primera aparición de ese número o -1 si no se encuentra.
    for i in range(len(array)):
        if array[i] == numero:
            return i+1
    return -1
lista = [1,2,3,4,5,6,7,8,9,10]
print(buscar_valor(lista,10))