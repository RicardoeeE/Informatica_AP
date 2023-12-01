# Solicitar al usuario el número de filas y columnas
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear una matriz vacía
matriz = []

# Llenar la matriz con valores ingresados por el usuario
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = input(f"Ingrese el valor para la posición [{i}][{j}]: ")
        fila.append(valor)
    matriz.append(fila)

# Imprimir la matriz
print("Matriz resultante:")
for fila in matriz:
    print(fila)