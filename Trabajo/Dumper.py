import stl
import vtkplotlib as vpl
import numpy as np
from copy import deepcopy

cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl") 
rueda_delantera_derecha = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_derecha.stl") 
rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl") 
rueda_trasera_derecha = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_trasera_derecha.stl") 
rueda_trasera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_trasera_izquierda.stl") 

# Concatenamos las matrices de vértices y caras de los modelos.
origen = stl.mesh.Mesh(np.concatenate([cabina.data, rueda_delantera_derecha.data, rueda_delantera_izquierda.data, rueda_trasera_derecha.data,rueda_trasera_izquierda.data]))

def translate(translation): 
    matrix= np.identity(4) 
    matrix[0:3, 3] =translation 
    return matrix

Rz = Ry = Rx = np.identity(4)

rueda_delantera_izquierda_copia = deepcopy(rueda_delantera_izquierda)
Tl= translate([1.3, -0.1, 1.2])
Tf = Tl @ Rz @ Ry @ Rx
rueda_delantera_izquierda_copia.transform(Tf)
vpl.mesh_plot(rueda_delantera_izquierda_copia)


rueda_delantera_derecha_copia = deepcopy(rueda_delantera_derecha)
Tl= translate([1.3, -0.1, 1.2])
Tf = Tl @ Rz @ Ry @ Rx
rueda_delantera_derecha_copia.transform(Tf)
vpl.mesh_plot(rueda_delantera_derecha_copia)


rueda_trasera_izquierda_copia = deepcopy(rueda_trasera_izquierda)
Tl= translate([1.3, -0.1, 1.2])
Tf = Tl @ Rz @ Ry @ Rx
rueda_trasera_izquierda_copia.transform(Tf)
vpl.mesh_plot(rueda_trasera_izquierda_copia)


rueda_trasera_derecha_copia = deepcopy(rueda_trasera_derecha)
Tl= translate([1.3, -0.1, 1.2])
Tf = Tl @ Rz @ Ry @ Rx
rueda_trasera_derecha_copia.transform(Tf)
vpl.mesh_plot(rueda_trasera_derecha_copia)


mesh_actor = vpl.mesh_plot(origen)
vpl.show()
