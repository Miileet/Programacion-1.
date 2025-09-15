def mostrar_menu():
    print("\n\n\n\n1. Cargar títulos y ejemplares\n2. Mostrar catálogo completo\n3. Consultar disponibilidad\n4. Listar títulos agotados\n5. Agregar un nuevo título\n6. Actualizar ejemplares (préstamo/devolución)\n7. Salir\n\n ")

def cargar_titulos(titulos, ejemplares, cantidad_de_libros):
    while cantidad_de_libros < 20: 
        titulo = input("Ingrese el titulo(o FIN para salir)\n- - ->: ")
        if titulo.upper() == "FIN":
            break
        cantidad = int(input("Ingrese la cantidad de ejemplares\n- - ->: "))

        titulos[cantidad_de_libros] = titulo
        ejemplares[cantidad_de_libros] = cantidad
        cantidad_de_libros += 1
    return cantidad_de_libros

def mostrar_catalogo(titulos, ejemplares, cantidad_de_libros):
    for i in range(cantidad_de_libros):
        print(f"{titulos[i]} -> {ejemplares[i]} copias")

def disponibilidad(titulos, ejemplares, cantidad_de_libros):
    titulo = input("Ingrese el titulo a consultar\n- - ->: ")
    for i in range(cantidad_de_libros):
        if titulos[i].lower() == titulo.lower():
            print(f"{titulos[i]} tiene {ejemplares[i]} copias")
            return
    print("Titulo no encontrado")


def titulos_agotados(titulos, ejemplares, cantidad_de_libros):
    agotados = 0
    for i in range(cantidad_de_libros):
        if ejemplares[i] == 0:
            print(f"{titulos[i]} agotado")
            agotados += 1
    if agotados == 0:
        print("No hay libros agotados")

def agregar_titulo(titulos, ejemplares, cantidad_de_libros):
    if cantidad_de_libros >= 20:
        print("No se pueden agregar mas libros")
        return cantidad_de_libros
    
    titulo = input("ingrese el nombre del titulo\n- - ->: ")
    cantidad = int(input("Ingrese la cantidad de ejemplares\n- - ->: "))

    titulos[cantidad_de_libros] = titulo
    ejemplares[cantidad_de_libros] = cantidad
    cantidad_de_libros += 1
    print("Titulo agregado")
    return cantidad_de_libros


def actualizar_ejemplares(titulos, ejemplares, cantidad_de_libros):
    titulo = input("Ingrese el titulo\n- - ->: ")
    for i in range(cantidad_de_libros):
        if titulos[i].lower() == titulo.lower():
            cambio = int(input("Ingresa un numero. ingrsa un numero positivo para hacer una devolucion, o uno negativo para hacer un prestamo\n- - ->: "))
            ejemplares[i] += cambio
            if ejemplares[i] < 0: 
                ejemplares[i] = 0
            print(f"Ejemplares de {titulos[i]} actulizado a {ejemplares[i]}")
            return
    print("titulo no encontrado")

