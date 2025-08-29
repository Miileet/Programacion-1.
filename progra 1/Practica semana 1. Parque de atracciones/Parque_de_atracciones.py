# 1. Ingreso de datos secuenciales
# ○ Pedir el nombre y edad de un visitante.
# ○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña
# Rusa, Casa del Terror y Carrusel).
# 2. Uso de condicionales
# ○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más).
# ○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel.
# ○ Los demás pueden acceder a todas las atracciones.
# 3. Uso de ciclos
# ○ Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir o no según
# su edad.
# ○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror =
# $1200, Carrusel = $800).
# 4. Salida de resultados
# ○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo
# usar y el costo total a pagar.



nombre = input("Cual es su nombre?\n- - ->: ")
edad = int(input("Cual es su edad?\n- - ->: "))
atracciones = int(input("A que atraccion desea subir?\n1)Montaña rusa\n2)Casa del terror\n3)Carrusel\n- - ->: "))

match atracciones:
    case 1:
        if edad >= 12:
            print("Puede subirse a la montaña rusa")
        else: 
            print("No tiene edad para subir a la montaña rusa")
    case 2:
        if edad >= 18:
            print("Puede acceder a la casa del terror")
        else:
            print("No tiene edad para acceder a la casa del terror")
    case 3:
        if edad < 6:
            print("Puede acceder al carrusel")
        else:
            print("No tiene edad para subir al carrusel")

