import stl
import vtkplotlib as vpl
import numpy as np
from copy import deepcopy


def transform_and_plot(mesh, translation, rotation_matrix):
    mesh_copy = deepcopy(mesh)
    transformation_matrix = translate(translation) @ rotation_matrix
    mesh_copy.transform(transformation_matrix)
    vpl.mesh_plot(mesh_copy)
    return mesh_copy

def translate(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

Rz = Ry = Rx = np.identity(4)

def dumper():
    # Carga de modelos
    escenario = stl.mesh.Mesh.from_file("Trabajo/Stl/escenario.stl") 
    cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl")
    rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl")

    # Concatenación de matrices de vértices y caras
    origen = stl.mesh.Mesh(np.concatenate([cabina.data]*4))

    # Par ruedas delante y atrás:
    def plot_wheel(translation):
        wheel_copy = deepcopy(rueda_delantera_izquierda)
        Tl = translate(translation)
        Tf = Tl @ Rz @ Ry @ Rx
        wheel_copy.transform(Tf)
        vpl.mesh_plot(wheel_copy)

    plot_wheel([1.3, -0.1, 1.2])
    plot_wheel([1.3, -0.1, -1.2])
    plot_wheel([-1.4, -0.1, 1.2])
    plot_wheel([-1.4, -0.1, -1.2])

    # Visualización final
    vpl.view(camera_position=(32.5, 20, 120), focal_point=(32.5, 0, 0))

    # Configuración de ejes
    vpl.plot(np.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=10.0, label="X")
    vpl.plot(np.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=10.0, label="Y")
    vpl.plot(np.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=10.0, label="Z")

    # Visualización

    mesh_actor = vpl.mesh_plot(origen)
    vpl.mesh_plot(escenario)
    vpl.view(camera_position=(32.5, 20, 120), focal_point=(32.5, 0, 0))
    vpl.show()

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

# Cargar una nueva instancia de rueda delantera derecha
rueda_delantera_derecha_copia2 = transform_and_plot(rueda_delantera_derecha, [1.3, -0.1, -1.2], Rz @ Ry @ Rx @ translate([5.0, 0.0, 0.0]))

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
    rueda_d = deepcopy(rueda_delantera_derecha)
    Tl = translate([1.3, -0.1, -1.2])
    Tf = (Tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_d.transform(Tf)
    paint([cab, rueda_i, rueda_d])

# Visualización final
vpl.mesh_plot(cab)
vpl.mesh_plot(rueda_i)
vpl.mesh_plot(rueda_d)

mesh_actor = vpl.mesh_plot(origen)
vpl.show()
