# Ejercicio uno:
diccionario1={"pera":"1.25","naranja":"1.70","manzana":"1.55","kiwi":"2.90","mandarina":"1.19","fresa":"1.25"}

def main():
    print("---Precios para hoy---")
    for clave in diccionario1.keys():
        print(f"{clave}: {diccionario1[clave]}")
    print("------------------------")

    fruta = input("Qué fruta quieres: ")
    pedir_fruta(fruta)
    

def pedir_fruta(fruta):
    if fruta not in diccionario1.keys() :
        print("Dicha fruta no es una opción valida, o no está en nuestra tienda")
    else:
        kg = float(input("cuantos kg quieres: "))
    while kg < 0:
        kg = float(input("Dame una cantiad correcta: ")) 
    pedir_cantidad(kg) 

def pedir_cantidad(kg):
    indice = diccionario1.index(pedir_fruta)
    precio = diccionario1[indice]
    print (f"{kg} kg de pera cuesttan {kg*precio}")


if __name__=="__main__":
    main()