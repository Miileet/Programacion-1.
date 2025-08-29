def mostrar_atracciones():
    print("""
    1)Montaña rusa (1500$)
    2)Casa del terror (1200%)
    3)Carrusel (800$)
        """)

def puede_subir(edad:int, atraccion:str)->bool:
    acceso = True
    match atraccion:
        case 1:
            if edad >= 12:
                acceso = True
            else: 
                acceso = False
        case 2:
            if edad >= 18:
                acceso = True
        case 3:
            if edad < 6:
                acceso = True
            else:
                acceso = False

    return acceso


def calcular_precio(atraccion:int)->int:
    precio = 0
    match atraccion:
        case 1:
            precio = 1500
        case 2:
            precio = 1200
        case 3:
            precio = 800
    return precio


def registrar_visita():
    nombre = input("¿Cuál es su nombre?\n- - ->: ")
    edad = int(input("¿Cuál es su edad?\n- - ->: "))
    mostrar_atracciones()
    atraccion = int(input("Elija una atracción (1-3)\n- - ->: "))

    if atraccion == 1:
        atr = "Montaña rusa"
    elif atraccion == 2:
        atr = "Casa del terror"
    elif atraccion == 3:
        atr = "Carrusel"
    if puede_subir(edad, atraccion):
        subio = 0
        precio = calcular_precio(atraccion)
        mensaje = "Acceso permitido"
        subio = 1
    else:
        precio = 0
        mensaje = "No cumple con la edad para subir"
        subio = 0

    return nombre, edad, atr, precio, mensaje, subio

def mostrar_resumen(nombre, edad, atraccion, precio, mensaje):
    print("\n--- Resumen de visita ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"atracción elegida: {atraccion}")
    print(f"Precio: {precio}$")
    print(mensaje)