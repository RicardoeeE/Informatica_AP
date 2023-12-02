import tkinter as tk
from tkinter import messagebox
import numpy as np
import stl
import vtkplotlib as vpl

#Archivo "main" principal del programa 
#Uso esta extructura de metodos y emcapsulado porque me gusta y soy capaz de ello ;) (obviamente es como se programa en la realidad, eficiencia, limpieza,....)

def main():
    # Cargar ventana bienvenida 
    # Coloca aquí el código para iniciar el simulador
    messagebox.showinfo("Simulador de Dumpers", "Simulador iniciado")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Dumpers")

# Crear una etiqueta con el mensaje de bienvenida
etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido al simulador de dumpers, pulsa para iniciar:")
etiqueta_bienvenida.pack(padx=10, pady=10)

# Crear un botón para iniciar el simulador
boton_iniciar = tk.Button(ventana, text="Iniciar")
boton_iniciar.pack(padx=10, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
