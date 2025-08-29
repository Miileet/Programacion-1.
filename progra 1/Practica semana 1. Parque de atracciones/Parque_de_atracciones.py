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
visitas = int(input("¿Cuántas atracciones quiere usar?\n- - ->: "))
atracciones_elegidas = ""
atracciones_usadas = ""

costo_total = 0
for i in range(visitas):
    atracciones = int(input("A que atraccion desea subir?\n1)Montaña rusa\n2)Casa del terror\n3)Carrusel\n- - ->: "))
    match atracciones:
        case 1:
            atracciones_elegidas += "Montaña Rusa, "
            if edad >= 12:
                print("Puede subirse a la montaña rusa")
                costo_total += 1500
                atracciones_usadas += "Montaña Rusa, "
            else: 
                print("No tiene edad para subir a la montaña rusa")
        case 2:
            atracciones_elegidas += "Casa del Terror, "
            if edad >= 18:
                print("Puede acceder a la casa del terror")
                costo_total += 1200
                atracciones_usadas += "Casa del Terror, "
            else:
                print("No tiene edad para acceder a la casa del terror")
        case 3:
            atracciones_elegidas += "Carrusel, "
            if edad < 6:
                print("Puede acceder al carrusel")
                costo_total += 800
                atracciones_usadas += "Carrusel, "


print(f"\n--- Resumen de visita ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"precio final: {costo_total}$")
print(f"Atracciones a las que pudo subir: {atracciones_usadas}")
print(f"Atracciones elegidas: {atracciones_elegidas}")
