import numpy as np
from copy import deepcopy
import stl
import vtkplotlib as vpl

def translate(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

Rz = Ry = Rx = np.identity(4)

def main():
    # Carga de modelos
    escenario = stl.mesh.Mesh.from_file("Trabajo/Stl/escenario.stl") 
    cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl")
    rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl")

    # Concatenación de matrices de vértices y caras
    origen = stl.mesh.Mesh(np.concatenate([cabina.data, 
                                           rueda_delantera_izquierda.data]*4))

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

    # Configuración de ejes
    vpl.plot(np.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=10.0, label="X")
    vpl.plot(np.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=10.0, label="Y")
    vpl.plot(np.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=10.0, label="Z")

    # Visualización
    mesh_actor = vpl.mesh_plot(origen)
    vpl.show()
    vpl.view(camera_position=(32.5, 20, 120), focal_point=(32.5, 0, 0))

if __name__ == "__main__":
    main()
