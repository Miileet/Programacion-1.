from parque import *

visitas = int(input("Cuantas atracciones desea intentar subir?\n- - ->:  "))
total_precio = 0
total_subidas = 0

for i in range(visitas):
    print(f"\n--- Registro de visita {i+1} ---")
    nombre, edad, atraccion, precio, mensaje, subio = registrar_visita()
    mostrar_resumen(nombre, edad, atraccion, precio, mensaje)

    total_precio += precio
    total_subidas += subio



if total_subidas >= 3:
    total_precio *= 0.9
    print("Tuviste un descuento del 10% por subir a mas de 3 atracciones")
print(f"Subiste a un total de {total_subidas} atracciones")
print(f"Preciofinal es: {total_precio}")