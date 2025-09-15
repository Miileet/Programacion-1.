from funciones import *
from constantes import *

pregunta = 0 
cantidad_de_libros = 0
while pregunta != 7: 
    mostrar_menu()
    pregunta = int(input("Seleccione una opcion\n- - ->: "))
    match pregunta:
        case 1:
            cantidad_de_libros = cargar_titulos(titulos, ejemplares, cantidad_de_libros)
        case 2:
            mostrar_catalogo(titulos, ejemplares, cantidad_de_libros)
        case 3:
            disponibilidad(titulos, ejemplares, cantidad_de_libros)
        case 4:
            titulos_agotados(titulos, ejemplares, cantidad_de_libros)
        case 5:
            cantidad_de_libros = agregar_titulo(titulos, ejemplares, cantidad_de_libros)
        case 6: 
            actualizar_ejemplares(titulos, ejemplares, cantidad_de_libros)
        case 7:
            print("Adios")
        case _:
            print("opcion invlida")