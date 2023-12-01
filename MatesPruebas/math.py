"""
Este es un módulo de ejemplo que contiene funciones matemáticas.
Puedes utilizar las funciones de este módulo para realizar cálculos matemáticos.
"""
# Aquí comienza el código del módulo

import numpy as np
import matplotlib.pyplot as plt

# Función Racional en Coordenadas Cilíndricas (ρ, θ, z)
rho_rational = np.linspace(0.1, 5, 400)
theta_rational = np.linspace(0, 2*np.pi, 400)
z_rational = np.linspace(-5, 5, 400)

# Crear una malla tridimensional de coordenadas cilíndricas
Rho, Theta, Z = np.meshgrid(rho_rational, theta_rational, z_rational, indexing='ij')

# Definir una función en coordenadas cilíndricas
# En este ejemplo, utilizaremos una función simple
# f(ρ, θ, z) = ρ * np.sin(θ) + z
f_cylindrical = Rho * np.sin(Theta) + Z

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la función en coordenadas cilíndricas
ax.plot_surface(Rho[0], Theta[0], f_cylindrical[0], cmap='viridis')

# Configurar etiquetas de ejes
ax.set_xlabel('ρ * cos(θ)')
ax.set_ylabel('ρ * sin(θ)')
ax.set_zlabel('f(ρ, θ, z)')

# Título
plt.title('Función en Coordenadas Cilíndricas')

plt.show()
