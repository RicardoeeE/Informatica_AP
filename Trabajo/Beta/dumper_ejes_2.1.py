import numpy as np
from copy import deepcopy
import stl
import vtkplotlib as vpl

def main():
    # Carga de modelos
    cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl")
    rueda_delantera_derecha = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_derecha.stl")
    rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl")
    rueda_trasera_derecha = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_trasera_derecha.stl")
    rueda_trasera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_trasera_izquierda.stl")

    # Concatenación de matrices de vértices y caras
    origen = stl.mesh.Mesh(np.concatenate([cabina.data, rueda_delantera_derecha.data,
                                           rueda_delantera_izquierda.data, rueda_trasera_derecha.data,
                                           rueda_trasera_izquierda.data]))

    # Definición de función de traslación
    def translate(translation):
        matrix = np.identity(4)
        matrix[0:3, 3] = translation
        return matrix

    Rz = Ry = Rx = np.identity(4)

    # Par ruedas delante:
    def plot_wheel(translation):
        # AL ser reudas iguales pues copio solo una y la uso para las 4,
        #  obviamente así saturo menos las llamadas a buscar el archivo (lo dejo declarado las 4 por si las uso en el giro)
        wheel_copy = deepcopy(rueda_delantera_izquierda)
        Tl = translate(translation)
        Tf = Tl @ Rz @ Ry @ Rx
        wheel_copy.transform(Tf)
        vpl.mesh_plot(wheel_copy)

    plot_wheel([1.3, -0.1, 1.2])
    plot_wheel([1.3, -0.1, -1.2])

    # Par ruedas atrás:
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
