opciones = ["(1) Añadir paltaformas",
            "(2) Eliminar plataformas",
            "(3) Mostrar precio plataforma",
            "(4) Lista plataformas",
            "(5) Subscribirse n meses a una plataforma ",
            "(6) Terminar"]

palataformas = {
    "Netflix": 11.99,
    "HBO": 8.99,
    "Movistar": 85,
    "Disney+": 7,
    "DAZN": 9.99,
    "Spotify": 9.99,
    "Apple Music": 9.99,
    "Amazon Prime": 3.99,
}
def main():
    for opcion in opciones:
        print(opcion)
    opcion_seleccionada = input("Elige una opcion: ")

    if opcion_seleccionada in range (1, len(opciones)+1):
        print("Ha seleccioando la opción "+ opciones[opcion_seleccionada-1])
    else:
        print("La opción selecionada no es valida")


if __name__=="__main__":
    main()