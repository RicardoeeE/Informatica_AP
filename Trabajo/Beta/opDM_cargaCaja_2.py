import stl
import vtkplotlib as vpl
import time
import numpy as np
from copy import deepcopy

time.sleep(1)
def load_mesh(file_path):
    return stl.mesh.Mesh.from_file(file_path)

def translate(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

def transform_and_plot(mesh, translation, rotation_matrix):
    mesh_copy = deepcopy(mesh)
    transformation_matrix = translate(translation) @ rotation_matrix
    mesh_copy.transform(transformation_matrix)
    vpl.mesh_plot(mesh_copy)
    return mesh_copy

def paint(dumper):
    lista = [vpl.mesh_plot(piece) for piece in dumper]
    figure = vpl.gcf()
    figure.update()
    figure.show(block=False)
    for piece in lista:
        figure.remove_plot(piece)

# Inicialización de matrices de rotación
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
                                       ]*2))

# Visualización del escenario
vpl.QtFigure()        
vpl.mesh_plot(escenario)

# Inicialización de transformaciones
Tf_cabina = np.identity(4)
Tf_rueda = translate([1.3, -0.1, 1.2])

# Ajuste de velocidad de animación
animation_speed = 0.1

# Animación de la máquina moviéndose
n_steps = 150
for step in range(n_steps):
    x = step * 50.0 / n_steps
    
    # Transformación de la cabina
    Tl = translate([x, 0.0, 0.0])
    Tf_cabina = Tl @ Rz @ Ry @ Rx
    
    # Transformación de las ruedas
    Tf_rueda = Tl @ Tf_rueda
    
    # Aplicar transformaciones a las instancias existentes
    cabina.transform(Tf_cabina)
    rueda_delantera_izquierda.transform(Tf_rueda)
    
    # Pintar la escena en cada paso
    paint([cabina, rueda_delantera_izquierda])
    
    # Añadir un pequeño retraso para ajustar la velocidad de la animación
    vpl.pause(animation_speed)

# Visualización final
cab_final = deepcopy(cabina)
cab_final.transform(Tf_cabina)

rueda_final = deepcopy(rueda_delantera_izquierda)
rueda_final.transform(Tf_rueda)

vpl.mesh_plot(cab_final)
vpl.mesh_plot(rueda_final)
vpl.show()
