import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use("TkAgg")  # Cambia el backend a "TkAgg" (o "Qt5Agg" si prefieres) para VSC

# Parámetros de la animación
duration = 100  # Duración en segundos
fps = 30      # Cuadros por segundo

# Crear una figura y un eje
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Función de inicialización para la animación
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# Función de actualización para la animación
def update(frame):
    t = frame / fps  # Tiempo actual
    y = np.sin(x - t)  # Función senoidal que cambia con el tiempo
    line.set_ydata(y)
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=int(duration * fps), init_func=init, blit=True)

# Guardar la animación como un archivo GIF
ani.save('senoidal_animacion.gif', writer='pillow', fps=fps)
