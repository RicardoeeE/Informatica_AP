import stl
import vtkplotlib as vpl
import numpy as np
from copy import deepcopy

def cargar_fichero(file_path):
    return stl.mesh.Mesh.from_file(file_path)

def translacion(translation):
    matrix = np.identity(4)
    matrix[0:3, 3] = np.array(translation)
    return matrix

def rotate_x(angulo):
    radianes = np.radians(angulo)
    matrix_rotacion = np.array([
        [1, 0, 0, 0],
        [0, np.cos(radianes), -np.sin(radianes), 0],
        [0, np.sin(radianes), np.cos(radianes), 0],
        [0, 0, 0, 1]
    ])
    return matrix_rotacion

def rotate_y(angulo):
    radianes = np.radians(angulo)
    matrix_rotacion = np.array([
        [np.cos(radianes), 0, np.sin(radianes), 0],
        [0, 1, 0, 0],
        [-np.sin(radianes), 0, np.cos(radianes), 0],
        [0, 0, 0, 1]
    ])
    return matrix_rotacion

def rotate_z(angulo):
    radianes = np.radians(angulo)
    matrix_rotacion = np.array([
        [np.cos(radianes), -np.sin(radianes), 0, 0],
        [np.sin(radianes), np.cos(radianes), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return matrix_rotacion

Rz = Ry = Rx = np.identity(4)

def ubi_ruedas(traslacion):
    rueda_delantera_izquierda = cargar_fichero("Trabajo/Stl/rueda_delantera_izquierda.stl")
    wheel_copy = deepcopy(rueda_delantera_izquierda)
    tl = translacion(traslacion)
    Tf = tl @ Rz @ Ry @ Rx
    wheel_copy.transform(Tf)
    vpl.mesh_plot(wheel_copy)

def ubi_cubo(traslacion):
    cubo = cargar_fichero("Trabajo/Stl/Tanque_Mejor2.Stl")
    cubo_copy = deepcopy(cubo)
    tl = translacion(traslacion)
    Tf = tl @ Rz @ Ry @ Rx
    cubo_copy.transform(Tf)
    vpl.mesh_plot(cubo_copy)

def main():
    # Carga de modelos
    cabina = cargar_fichero("Trabajo/Stl/cabina.stl")
    escenario = cargar_fichero("Trabajo/Stl/escenario.stl") 
    rueda_delantera_izquierda = cargar_fichero("Trabajo/Stl/rueda_delantera_izquierda.stl")
    rueda_delantera_derecha = cargar_fichero("Trabajo/Stl/rueda_delantera_derecha.stl")
    rueda_trasera_izquierda = cargar_fichero("Trabajo/Stl/rueda_trasera_izquierda.stl")
    rueda_trasera_derecha = cargar_fichero("Trabajo/Stl/rueda_trasera_derecha.stl")
    cubo = cargar_fichero("Trabajo/Stl/Tanque_Mejor2.Stl")

    # Función para pintar la máquina
    def paint(dumper):
        lista = [vpl.mesh_plot(piece) for piece in dumper]
        figure = vpl.gcf()
        figure.update()
        figure.show(block=False)
        for piece in lista:
            figure.remove_plot(piece)

    # Par ruedas delante y atrás:
    ubi_ruedas([1.3, -0.1, 1.2])
    ubi_ruedas([1.3, -0.1, -1.2])
    ubi_ruedas([-1.4, -0.1, 1.2])
    ubi_ruedas([-1.4, -0.1, -1.2])

    # Llamada a la función para fijar la posición del tanque
    ubi_cubo([ -1.04, 0.63, 0])

    # Visualización del escenario
    vpl.QtFigure()        
    vpl.mesh_plot(escenario)

    # Animación de la máquina moviéndose
    n_steps = 150
    for step in range(n_steps):
        x = step * 55.0 / n_steps

        cab = deepcopy(cabina)
        tl = translacion([x, 0.0, 0.0])
        tf_cabina = tl @ Rz @ Ry @ Rx
        cab.transform(tf_cabina)

        rueda_i = deepcopy(rueda_delantera_izquierda)
        tl = translacion([1.3, -0.1, 1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_i.transform(tf)

        rueda_d = deepcopy(rueda_delantera_derecha)
        tl = translacion([1.3, -0.1, -1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_d.transform(tf)

        rueda_i2 = deepcopy(rueda_trasera_izquierda)
        tl = translacion([-1.4, -0.1, 1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_i2.transform(tf)

        rueda_d2 = deepcopy(rueda_trasera_derecha)
        tl = translacion([-1.4, -0.1, -1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_d2.transform(tf)

        cubo = deepcopy(cubo)
        tl = translacion([-1.04, 0.63, 0])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        cubo.transform(tf)

        paint([cab, rueda_i, rueda_d, rueda_i2, rueda_d2, cubo])

    

    posicion_final_recto=[55.0,0.0,0.0]
    # Radio del giro
    radio_giro = 11.0
    n_steps_giro = 60
    for step_giro in range(n_steps_giro):
        angulo_giro = step_giro * -90.0 / n_steps_giro  # Giro de 90 grados

        cab = deepcopy(cabina)
        rueda_i = deepcopy(rueda_delantera_izquierda)
        rueda_d = deepcopy(rueda_delantera_derecha)
        rueda_i2 = deepcopy(rueda_trasera_izquierda)
        rueda_d2 = deepcopy(rueda_trasera_derecha)
        cubo = deepcopy(cubo)

        # Calcula la posición en el círculo para hacer la trayectoria más circular
        x_circulo = posicion_final_recto[0] + radio_giro * -np.sin(np.radians(angulo_giro))
        z_circulo = posicion_final_recto[2] + radio_giro * (1 - np.cos(np.radians(angulo_giro)))

        # Traslada a la posición circular
        tl_circular = translacion([x_circulo, 0.0, z_circulo])

        # Aplica la rotación justo después de la translación circular
        tf_cabina = tl_circular @ rotate_y(angulo_giro) @ (Rz @ Ry @ Rx)
        tf_ruedas = tl_circular @ rotate_y(angulo_giro) @ Rz @ Ry @ Rx

        cab.transform(tf_cabina)
        rueda_i.transform(tf_ruedas)
        rueda_d.transform(tf_ruedas)
        rueda_i2.transform(tf_ruedas)
        rueda_d2.transform(tf_ruedas)
        cubo.transform(tf_cabina)

        paint([cab, rueda_i, rueda_d, rueda_i2, rueda_d2, cubo])

    # Animación de la máquina moviéndose post-giro
    n_steps = 120
    for step in range(n_steps):
        x = step * 33.0 / n_steps

        cab = deepcopy(cabina)
        tl = translacion([66, 0, x+11])
        tf_cabina = tl @ Rz @ Ry @ Rx
        cab.transform(tf_cabina)

        rueda_i = deepcopy(rueda_delantera_izquierda)
        tl = translacion([1.3, -0.1, 1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_i.transform(tf)

        rueda_d = deepcopy(rueda_delantera_derecha)
        tl = translacion([1.3, -0.1, -1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_d.transform(tf)

        rueda_i2 = deepcopy(rueda_trasera_izquierda)
        tl = translacion([-1.4, -0.1, 1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_i2.transform(tf)

        rueda_d2 = deepcopy(rueda_trasera_derecha)
        tl = translacion([-1.4, -0.1, -1.2])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        rueda_d2.transform(tf)

        cubo = deepcopy(cubo)
        tl = translacion([-1.04, 0.63, 0])
        tf = (tl @ Rz @ Ry @ Rx) @ tf_cabina
        cubo.transform(tf)

        paint([cab, rueda_i, rueda_d, rueda_i2, rueda_d2, cubo])

    # Visualización final
    vpl.mesh_plot(cab)
    vpl.mesh_plot(rueda_i)
    vpl.mesh_plot(rueda_d)
    vpl.mesh_plot(rueda_i2)
    vpl.mesh_plot(rueda_d2)
    vpl.mesh_plot(cubo)
    
    # Configuración de ejes
    vpl.plot(np.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=10.0, label="X")
    vpl.plot(np.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=10.0, label="Y")
    vpl.plot(np.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=10.0, label="Z")


    vpl.show()

if __name__ == "__main__":
    main()
