from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from login.ui import LoginUI

class MenuUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Menú Principal")
        self.window.config(bg="PaleTurquoise2")

        # Configuración de tamaño y posición de la ventana
        window_width = 1200
        window_height = 770
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = 0
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.window.resizable(False, False)

        # Crear label izquierdo
        label_width = window_width // 32
        self.label = Label(self.window, bg="RoyalBlue4", width=label_width, height=window_height)
        self.label.place(x=0, y=0)

        # Crear franja superior
        label_top_height = window_height // 235
        label_top_width = window_width
        self.label_top = Label(self.window, bg="SteelBlue3", width=label_top_width, height=label_top_height)
        self.label_top.place(x=0, y=0)
        self.label_top.lower()

        # Cargar y configurar imagen de "salir"
        self.salir_img = Image.open("menu/images/salir.png")
        self.salir_img_resized = self.salir_img.resize((90, 90))
        self.salir_img_tk = ImageTk.PhotoImage(self.salir_img_resized)

        # Crear botón "salir" en la parte superior derecha
        self.salir_button = Button(self.window, image=self.salir_img_tk, command=self.regresar_login, bd=0, bg='SteelBlue3', width=50, height=35)
        self.salir_button.place(x=window_width - 60, y=10)

    def regresar_login(self):
        self.window.destroy()
        from mainapp import open_login_window
        open_login_window()
