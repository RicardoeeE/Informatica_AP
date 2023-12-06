import vtkplotlib as vpl
import numpy as np
from copy import deepcopy

def transform_and_plot(mesh, translation, rotation_matrix):
    mesh_copy = mesh
    transformation_matrix = translate(translation) @ rotation_matrix
    mesh_copy.transform(transformation_matrix)
    vpl.mesh_plot(mesh_copy)
    return mesh_copy

def translate(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

def rotate_y(angle):
    """Create a transformation matrix for rotation over y axis."""
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, 0.0, s, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-s, 0.0, c, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

# Carga de modelos
escenario = stl.mesh.Mesh.from_file("Trabajo/Stl/escenario.stl") 
cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl")
rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl")
rueda_delantera_derecha = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_derecha.stl")

# Concatenación de matrices de vértices y caras
origen = stl.mesh.Mesh(np.concatenate([cabina.data, 
                                       rueda_delantera_derecha.data,
                                       rueda_delantera_izquierda.data]*2))

# Función para pintar la máquina
def paint(dumper):
    lista = [vpl.mesh_plot(piece) for piece in dumper]
    figure = vpl.gcf()
    figure.update()
    figure.show(block=False)
    for piece in lista:
        figure.remove_plot(piece)

# Par ruedas delante y atrás:
def hot_wheels(traslacion):
    Tl = translate(traslacion)
    Tf = Tl @ rotate_y(np.radians(90))  # Girar 90 grados sobre el eje Y
    rueda_copy_left = mesh_copy(rueda_delantera_izquierda)
    rueda_copy_right = mesh_copy(rueda_delantera_derecha)
    
    rueda_copy_left.transform(Tf)
    rueda_copy_right.transform(Tf)
    
    vpl.mesh_plot(rueda_copy_left)
    vpl.mesh_plot(rueda_copy_right)

# Visualización inicial de la máquina
hot_wheels([1.3, -0.1, 1.2])
hot_wheels([1.3, -0.1, -1.2])
hot_wheels([-1.4, -0.1, 1.2])
hot_wheels([-1.4, -0.1, -1.2])

# Visualización del escenario
vpl.QtFigure()        
vpl.mesh_plot(escenario)

# Animación de la máquina moviéndose y girando
n_steps = 150
for step in range(n_steps):
    x = step * 50.0 / n_steps
    cab = mesh_copy(cabina)
    Tl = translate([x, 0.0, 0.0])
    Tf_cabina = Tl @ rotate_y(np.radians(90))  # Girar 90 grados sobre el eje Y
    cab.transform(Tf_cabina)
    
    # Mantener las ruedas en su lugar relativo a la cabina
    rueda_copy_left = transform_and_plot(rueda_delantera_izquierda, [1.3 + x, -0.1, 1.2], Tf_cabina)
    rueda_copy_right
