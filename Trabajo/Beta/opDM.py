import stl
import vtkplotlib as vpl
import numpy as np
from copy import deepcopy

def cargar_fichero(file_path):
    return stl.mesh.Mesh.from_file(file_path)

def transformacion(mesh, translation, rotation_matrix):
    mesh_copy = deepcopy(mesh)
    transformation_matrix = translacion(translation) @ rotation_matrix
    mesh_copy.transform(transformation_matrix)
    vpl.mesh_plot(mesh_copy)
    return mesh_copy

def translacion(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

Rz = Ry = Rx = np.identity(4)

# Carga de modelos
cabina = cargar_fichero("Trabajo/Stl/cabina.stl")
escenario = cargar_fichero("Trabajo/Stl/escenario.stl") 
rueda_delantera_izquierda = cargar_fichero("Trabajo/Stl/rueda_delantera_izquierda.stl")
rueda_delantera_derecha = cargar_fichero("Trabajo/Stl/rueda_delantera_derecha.stl")
rueda_trasera_izquierda = cargar_fichero("Trabajo/Stl/rueda_trasera_izquierda.stl")
rueda_trasera_derecha = cargar_fichero("Trabajo/Stl/rueda_trasera_derecha.stl")
tanque = cargar_fichero("Trabajo/Stl/Tanque_Mejor2.Stl")


# Concatenación de matrices de vértices y caras
origen = stl.mesh.Mesh(np.concatenate([cabina.data, 
                                       rueda_delantera_derecha.data,
                                       rueda_delantera_izquierda.data,
                                       rueda_trasera_izquierda.data,
                                       rueda_trasera_derecha.data,
                                       tanque.data
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
def ubi_ruedas(traslacion):
    wheel_copy = deepcopy(rueda_delantera_izquierda)
    tl = translacion(traslacion)
    Tf = tl @ Rz @ Ry @ Rx
    wheel_copy.transform(Tf)
    vpl.mesh_plot(wheel_copy)

def rotate_z(angle):
    radian_angle = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(radian_angle), -np.sin(radian_angle), 0],
        [np.sin(radian_angle), np.cos(radian_angle), 0],
        [0, 0, 1]
    ])
    return rotation_matrix
def rotate_y(angle):
    radian_angle = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(radian_angle), 0, np.sin(radian_angle)],
        [0, 1, 0],
        [-np.sin(radian_angle), 0, np.cos(radian_angle)]
    ])
    return rotation_matrix
def rotate_x(angle):
    radian_angle = np.radians(angle)
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(radian_angle), -np.sin(radian_angle)],
        [0, np.sin(radian_angle), np.cos(radian_angle)]
    ])
    return rotation_matrix

ubi_ruedas([1.3, -0.1, 1.2])
ubi_ruedas([1.3, -0.1, -1.2])
ubi_ruedas([-1.4, -0.1, 1.2])
ubi_ruedas([-1.4, -0.1, -1.2])

# Visualización del escenario
vpl.QtFigure()        
vpl.mesh_plot(escenario)

# Animación de la máquina moviéndose
n_steps = 200
for step in range(n_steps):
    x = step * 66.0 / n_steps

    cab = deepcopy(cabina)
    tl = translacion([x, 0.0, 0.0])
    Tf_cabina = tl @ Rz @ Ry @ Rx
    cab.transform(Tf_cabina)

    rueda_i = deepcopy(rueda_delantera_izquierda)
    tl = translacion([1.3, -0.1, 1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_i.transform(Tf)

    rueda_d = deepcopy(rueda_delantera_derecha)
    tl = translacion([1.3, -0.1, -1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_d.transform(Tf)

    rueda_i2 = deepcopy(rueda_trasera_izquierda)
    tl = translacion([-1.4, -0.1, 1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_i2.transform(Tf)

    rueda_d2 = deepcopy(rueda_trasera_derecha)
    tl = translacion([-1.4, -0.1, -1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_d2.transform(Tf)

    tanque = deepcopy(tanque)
    tl = translacion([-1.04, 0.63, 0])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    tanque.transform(Tf)

    paint([cab, rueda_i, rueda_d, rueda_i2, rueda_d2, tanque])


        # Animación de la máquina moviéndose post-giro
n_steps = 120
for step in range(n_steps):
    x = step * 44.0 / n_steps

    cab = deepcopy(cabina)
    tl = translacion([66, 0, x])
    Tf_cabina = tl @ Rz @ Ry @ Rx
    cab.transform(Tf_cabina)

    rueda_i = deepcopy(rueda_delantera_izquierda)
    tl = translacion([1.3, -0.1, 1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_i.transform(Tf)

    rueda_d = deepcopy(rueda_delantera_derecha)
    tl = translacion([1.3, -0.1, -1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_d.transform(Tf)

    rueda_i2 = deepcopy(rueda_trasera_izquierda)
    tl = translacion([-1.4, -0.1, 1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_i2.transform(Tf)

    rueda_d2 = deepcopy(rueda_trasera_derecha)
    tl = translacion([-1.4, -0.1, -1.2])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    rueda_d2.transform(Tf)

    cubo = deepcopy(tanque)
    tl = translacion([-1.04, 0.63, 0])
    Tf = (tl @ Rz @ Ry @ Rx) @ Tf_cabina
    cubo.transform(Tf)

    paint([cab, rueda_i, rueda_d, rueda_i2, rueda_d2, cubo])


# Visualización final
vpl.mesh_plot(cab)
vpl.mesh_plot(rueda_i)
vpl.mesh_plot(rueda_d)
vpl.mesh_plot(rueda_i2)
vpl.mesh_plot(rueda_d2)
vpl.mesh_plot(cubo)

mesh_actor = vpl.mesh_plot(origen)
vpl.show()
