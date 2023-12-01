import stl
import vtkplotlib as vpl
# Cargamos el modelo desde un fichero con nombre "modelo.stl".
modelo = stl.mesh.Mesh.from_file("cabina.stl") # Crea la ventana (pero no la muestra). vpl.QtFigure()
# Añadimos la malla del objeto a la ventana. vpl.mesh_plot(modelo)
# Mostramos la ventana.
vpl.show()