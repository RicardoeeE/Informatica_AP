import numpy as np

def pedir(filColum):
    filColum = int(input("Dame el numero de filas y columnas (>0): "))

    while filColum == 0 or filColum < 0:
        filColum = int(input("ERROR, dame el numero de filas y columnas: (>0)"))

    return filColum


def calcular_matriz(filColum):
    matrizA = np.empty((filColum,filColum), dtype=np.int64)
    matrizB = np.empty((filColum,filColum), dtype=np.int64)

    for i in range(filColum):
        for j in range(filColum):
            elemento = int(input(f"A[{i},{j}]: "))
            matrizA[i,j] = elemento

    print("\n")
    print("Matriz A:")
    print(matrizA)
    print("\n")

    for i in range(filColum):
        for j in range(filColum):
            elemento = int(input(f"B[{i},{j}]: "))
            matrizB[i,j] = elemento

    print("\n")
    print("Matriz A:")
    print(matrizB)
    print("\n")

if __name__=="__name__":
    pedir()