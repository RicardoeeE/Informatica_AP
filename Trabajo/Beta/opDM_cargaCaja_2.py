import stl
import vtkplotlib as vpl
import numpy as np
from copy import deepcopy

def load_mesh(file_path):
    return stl.mesh.Mesh.from_file(file_path)

def transform_and_plot(mesh, translation, rotation_matrix):
    mesh_copy = deepcopy(mesh)
    transformation_matrix = translate(translation) @ rotation_matrix
    mesh_copy.transform(transformation_matrix)
    vpl.mesh_plot(mesh_copy)
    return mesh_copy

""""
cabina => [0.0, 0.0, 0.0]
plataforma_trasera => [0.0, 0.0, 0.0]
plataforma_de_giro => [-1.05, 0.25, 0.0]
cubo => [-1.04, 0.63, 0]
rueda_delantera_izquierda => [1.3, -0.1, 1.2]
rueda_delantera_derecha => [1.3, -0.1, -1.2]
rueda_trasera_izquierda => [-1.4, -0.1, 1.2]
rueda_trasera_derecha => [-1.4, -0.1, -1.2]
"""

def translate(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

Rz = Ry = Rx = np.identity(4)

# Carga de modelos
cabina = load_mesh("Trabajo/Stl/cabina.stl")
escenario = load_mesh("Trabajo/Stl/escenario.stl") 
rueda_delantera_izquierda = load_mesh("Trabajo/Stl/rueda_delantera_izquierda.stl")
caja = load_mesh("Trabajo/Stl/Tanque_Mejor2.STL")

# Concatenación de matrices de vértices y caras
origen = stl.mesh.Mesh(np.concatenate([cabina.data, 
                                       rueda_delantera_izquierda.data,
                                       caja.data,
                                       ]))

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
    wheel_copy = deepcopy(rueda_delantera_izquierda)
    Tl = translate(traslacion)
    Tf = Tl @ Rz @ Ry @ Rx
    wheel_copy.transform(Tf)
    vpl.mesh_plot(wheel_copy)

hot_wheels([1.3, -0.1, 1.2])
hot_wheels([1.3, -0.1, -1.2])
hot_wheels([-1.4, -0.1, 1.2])
hot_wheels([-1.4, -0.1, -1.2])

# Copia y transformación de la cabina
cabina_copia = transform_and_plot(cabina, [5.0, 0.0, 0.0], Rz @ Ry @ Rx)

# Copias y transformaciones de las ruedas delanteras
rueda_delantera_izquierda_copia2 = transform_and_plot(rueda_delantera_izquierda, [1.3, -0.1, 1.2], Rz @ Ry @ Rx @ translate([5.0, 0.0, 0.0]))


# Visualización del escenario
vpl.QtFigure()        
vpl.mesh_plot(escenario)

# Animación de la máquina moviéndose
n_steps = 150
for step in range(n_steps):
    x = step * 50.0 / n_steps
    cab = deepcopy(cabina)
    Tl = translate([x, 0.0, 0.0])
    Tf_cabina = Tl @ Rz @ Ry @ Rx
    cab.transform(Tf_cabina)
    rueda_i = deepcopy(rueda_delantera_izquierda)
    Tl = translate([1.3, -0.1, 1.2])
    Tf = (Tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_i.transform(Tf)
    paint([cab, rueda_i])

# Visualización final
vpl.mesh_plot(cab)
vpl.mesh_plot(rueda_i)

mesh_actor = vpl.mesh_plot(origen)
vpl.show()
