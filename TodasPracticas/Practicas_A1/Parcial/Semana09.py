a = int(input("Dame la longitud de la lista "))
def genera_completa(a):
    mi_lista = [None] * a
    for i in range(a):
        mi_lista[i] = input(f"Ingrese el elemento {i+1}: ")
    return mi_lista

    
lista_resultante = genera_completa(a)
print("Lista resultante: ", lista_resultante)

r = int(input("Dame las veces que se repiten "))
def repetir_lista(lista_resultante, r):
    lista_repeticon_uno = [elem for elem in lista_resultante for _ in range(r)]

    lista_repeticon_dos = lista_resultante * r

    return lista_repeticon_uno, lista_repeticon_dos
resultado_uno, resultado_dos = repetir_lista(lista_resultante,r)

print("Resutado 1:", resultado_uno)
print("Resutado 2:", resultado_dos)