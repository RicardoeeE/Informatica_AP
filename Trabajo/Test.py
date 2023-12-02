import stl
import vtkplotlib as vpl
import numpy as np

# Cargamos los modelos desde archivos STL.
cabina = stl.mesh.Mesh.from_file("Trabajo/Stl/cabina.stl") 
escenario = stl.mesh.Mesh.from_file("Trabajo/Stl/escenario.stl") 
rueda_delantera_derecha = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_derecha.stl") 
rueda_delantera_izquierda = stl.mesh.Mesh.from_file("Trabajo/Stl/rueda_delantera_izquierda.stl") 

# Concatenamos las matrices de vértices y caras de los modelos.
origen = stl.mesh.Mesh(np.concatenate([cabina.data, escenario.data, rueda_delantera_derecha.data, rueda_delantera_izquierda.data]))

# Creamos la figura y visualizamos la malla.
fig = vpl.QtFigure()

# Añadimos la malla al gráfico.
mesh_actor = vpl.mesh_plot(origen)

# Añadimos líneas desde el origen en colores diferentes.
lines_actor = vpl.plot([0, 1], [0, 0], [0, 0], 'red')  
lines_actor.set_line_width(2)

lines_actor = vpl.plot([0, 0], [0, 1], [0, 0], 'green')  
lines_actor.set_line_width(2)

lines_actor = vpl.plot([0, 0], [0, 0], [0, 1], 'blue')  
lines_actor.set_line_width(2)

# Mostramos la figura.
vpl.show()
