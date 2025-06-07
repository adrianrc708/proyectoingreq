import tkinter as tk
from login.ui import LoginUI
from menu.ui import MenuUI

def on_login_success():
    login_window.destroy()  # Cierra ventana de login
    open_menu_window()      # Abre ventana de menú

def open_menu_window():
    menu_window = tk.Tk()
    app = MenuUI(menu_window)
    menu_window.mainloop()  # Bucle principal de menú

def open_login_window():
    global login_window
    login_window = tk.Tk()
    app = LoginUI(login_window, on_success_callback=on_login_success)
    login_window.mainloop()  # Bucle principal de login

if __name__ == "__main__":
    open_login_window()  # Inicia ventana de login
