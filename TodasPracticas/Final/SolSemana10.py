import numpy as np
matriz_a = np.array([[3,5],[2,2]])
matriz_b = np.array([[3,5],[2,2]])
filas, columanas = matriz_a.shape
    
def mostrar_matriz(matriz):
    filas, columnas = matriz_a.shape
    matriz_c = np.empty((filas,columnas), dtype=int)


    for i in range(filas):
        for j in range (columnas):
            if matriz_a[i,j]== matriz_b[i,j]:
                matriz_c[i,j]=1
            else:
                matriz_c[i,j]=0
    return matriz_c

def main():
    matriz_a = np.array([[3,5],[2,2]])
    matriz_b = np.array([[3,5],[2,2]])
    matriz_c = crear_matriz_c(matriz_a,matriz_b)

    print("Matriz A:")
    mostrar_matriz(motriz)



