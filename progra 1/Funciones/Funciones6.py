    # 6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva 
    # cuántas horas y minutos sobran. 


def convertir_minutos(minutos:int):
        if minutos > 60:
            horas = minutos / 60
            mins = minutos % 60
            print(f"La cantidad de horas en {minutos} es de {horas:.0f}, y minutos {mins} ")
        else:
            print(f"Hay {minutos} minutos.")





minutos = int(input("Diga un numero\n- - ->: "))
convertir_minutos(minutos)