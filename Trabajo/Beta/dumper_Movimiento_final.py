import stl
import vtkplotlib as vpl
import numpy as np
from copy import deepcopy

cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl") 
escenario =stl.mesh.Mesh.from_file("Trabajo/Stl/escenario.stl")
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


vpl.QtFigure()
vpl.mesh_plot(cabina)
vpl.mesh_plot(rueda_delantera_izquierda_copia)
vpl.mesh_plot(rueda_delantera_derecha_copia)
cabina_copia=deepcopy(cabina)
Tl =translate([5.0, 0.0, 0.0])
Tf_cabina=Tl @Rz@Ry@Rx
cabina_copia.transform(Tf_cabina)
vpl.mesh_plot(cabina_copia)
rueda_delantera_izquierda_copia2 =deepcopy(rueda_delantera_izquierda)
Tl =translate([1.3, -0.1, 1.2])
Tf=(Tl @Rz@Ry@Rx) @Tf_cabina
rueda_delantera_izquierda_copia2.transform(Tf)
vpl.mesh_plot(rueda_delantera_izquierda_copia2)
rueda_delantera_derecha_copia2 =deepcopy(rueda_delantera_derecha)
Tl =translate([1.3, -0.1, -1.2])
Tf=(Tl @Rz@Ry@Rx) @Tf_cabina
rueda_delantera_derecha_copia2.transform(Tf)
vpl.mesh_plot(rueda_delantera_derecha_copia2)

def paint(maquina):
    lista = []
    for pieza in maquina:
        lista.append(vpl.mesh_plot(pieza))
    figure =vpl.gcf()
    figure.update()
    figure.show(block=False)
    for pieza in lista:
        figure.remove_plot(pieza)

vpl.QtFigure()        
vpl.mesh_plot(escenario)
n_steps=350
for step in range(n_steps):
    x =step *50.0/n_steps
    cab=deepcopy(cabina)
    Tl =translate([x, 0.0, 0.0])
    Tf_cabina=Tl @Rz@Ry@Rx
    cab.transform(Tf_cabina)
    rueda_i=deepcopy(rueda_delantera_izquierda)
    Tl =translate([1.3, -0.1, 1.2])
    Tf=(Tl @Rz@Ry@Rx) @Tf_cabina
    rueda_i.transform(Tf)
    rueda_d=deepcopy(rueda_delantera_derecha)
    Tl =translate([1.3, -0.1, -1.2])
    Tf=(Tl @Rz@Ry@Rx) @Tf_cabina
    rueda_d.transform(Tf)
    paint([cab, rueda_i, rueda_d])

vpl.mesh_plot(cab)
vpl.mesh_plot(rueda_i)
vpl.mesh_plot(rueda_d)

mesh_actor = vpl.mesh_plot(origen)
vpl.show()
