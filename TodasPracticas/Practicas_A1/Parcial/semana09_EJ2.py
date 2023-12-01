a = int(input("Dime el numero de elementos: "))
def genera_completa(a):
    mi_lista = [None] * a
    for i in range(a):
        mi_lista[i] = input(f"Introduce el valor del elemento {i+1}: ")
    return mi_lista

    
lista_resultante = genera_completa(a)
print("Lista resultante: ", lista_resultante)

# pares = [numero for numero in lista_resultante if numero % 2 == 0]

pares = [elemento for elemento in lista_resultante  if elemento % 2 == 0]



impares = [numero for numero in lista_resultante if numero % 2 != 0]

print("El primer vector es: ", pares)
print("El segundo vector es: ", impares)

