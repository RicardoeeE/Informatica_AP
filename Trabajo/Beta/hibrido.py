import numpy as np
from copy import deepcopy
import stl
import vtkplotlib as vpl

def translate(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = translation
    return matrix

Rz = Ry = Rx = np.identity(4)

    # Carga de modelos
escenario = stl.mesh.Mesh.from_file("Trabajo/Stl/escenario.stl") 
cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl")
rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl")
origen = stl.mesh.Mesh(np.concatenate([cabina.data, rueda_delantera_izquierda.data]*4))


def plot_wheel(translation, wheel_mesh):
    wheel_copy = deepcopy(wheel_mesh)
    Tl = translate(translation)
    Tf = Tl @ Rz @ Ry @ Rx
    wheel_copy.transform(Tf)
    vpl.mesh_plot(wheel_copy)

def main():

    # Par ruedas delante y atrás:
    plot_wheel([1.3, -0.1, 1.2], rueda_delantera_izquierda)
    plot_wheel([1.3, -0.1, -1.2], rueda_delantera_izquierda)
    plot_wheel([-1.4, -0.1, 1.2], rueda_delantera_izquierda)
    plot_wheel([-1.4, -0.1, -1.2], rueda_delantera_izquierda)

    # Configuración de ejes
    vpl.plot(np.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=10.0, label="X")
    vpl.plot(np.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=10.0, label="Y")
    vpl.plot(np.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=10.0, label="Z")

    # Visualización
    mesh_actor = vpl.mesh_plot(origen)

def paint(machine):
    lista = []
    for piece in machine:
        lista.append(vpl.mesh_plot(piece))
    figure = vpl.gcf()
    figure.update()
    figure.show(block=False)
    for piece in lista:
        figure.remove_plot(piece)

def animate_machine(n_steps=350):
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
        rueda_d = deepcopy(rueda_delantera_izquierda)
        Tl = translate([1.3, -0.1, -1.2])
        Tf = (Tl @ Rz @ Ry @ Rx) @ Tf_cabina
        rueda_d.transform(Tf)
        paint([cab, rueda_i, rueda_d])

    vpl.mesh_plot(cab)
    vpl.mesh_plot(rueda_i)
    vpl.mesh_plot(rueda_d)

    mesh_actor = vpl.mesh_plot(origen)
    vpl.show()

if __name__ == "__main__":
    main()
    animate_machine()
