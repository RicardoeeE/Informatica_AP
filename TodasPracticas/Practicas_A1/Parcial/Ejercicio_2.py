# Ejercicio dos:
import math
valor_pi = math.pi
print("====================================================")
print("\n")

radio = float(input("Introduce el radio: "))
altura = float(input("Introduce la altura: "))

def calcular_Superficie(radio, altura):
    resultado_Superficie =  2 * valor_pi * (radio + altura)
    return resultado_Superficie

superficie_format= "{:.3f}".format(calcular_Superficie(radio,altura))


def calcular_Volumen(radio, altura):
    resultado_Volumen = valor_pi * radio ** 2 + altura
    return resultado_Volumen

Volumen_format= "{:.3f}".format(calcular_Volumen(radio,altura))

print("\n")
print("La superficie es: " + superficie_format)
print("El volumen es:  " + Volumen_format)

print("\n")
print("====================================================")

