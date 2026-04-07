from funciones import (
    cargar_datos,
    listar_partidos,
    contar_amarillas,
    buscar_partidos_equipo,
    buscar_goles_jugador,
    clasificacion_por_goles,
)

MENU = """
          EUROCOPA 2024 - MENU PRINCIPAL
-------------------------------------------------
  1. Listar todos los partidos                
  2. Tarjetas amarillas (total y por equipo)  
  3. Buscar partidos de un equipo             
  4. Buscar goles de un jugador               
  5. Clasificacion por goles                  
  0. Salir                                    

"""
def main():
    datos = cargar_datos("euro_modificado.json")
    print("\n  Bienvenido al gestor de " + datos["name"])

    opcion = ""
    while opcion != "0":
        print(MENU)
        opcion = input("  Elige una opcion: ").strip()

        if opcion == "1":
            listar_partidos(datos)

        elif opcion == "2":
            contar_amarillas(datos)

        elif opcion == "3":
            equipo = input("  Introduce el nombre del equipo: ")
            buscar_partidos_equipo(datos, equipo)

        elif opcion == "4":
            jugador = input("  Introduce el nombre del jugador: ")
            buscar_goles_jugador(datos, jugador)

        elif opcion == "5":
            clasificacion_por_goles(datos)

        elif opcion != "0":
            print("\n  Opcion no valida. Introduce un numero del 0 al 5.\n")

    print("\n  Hasta pronto!\n")


if __name__ == "__main__":
    main()