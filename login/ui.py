from tkinter import *
from PIL import Image, ImageTk
from login.logic import validar_login


class LoginUI:
    def __init__(self, window, on_success_callback=None):
        # Inicializar ventana y callback de éxito
        self.window = window
        self.on_success_callback = on_success_callback
        self.window.title("Login")

        try:
            # Configurar la imagen de fondo
            self.img = Image.open("login/images/background.jpg")
            window_width = 400
            window_height = 550
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)
            self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
            self.window.resizable(False, False)

            # Crear canvas con la imagen de fondo
            self.img_resized = self.img.resize((window_width, window_height))
            self.img_tk = ImageTk.PhotoImage(self.img_resized)
            self.canvas = Canvas(self.window, width=window_width, height=window_height, highlightthickness=0, bd=0)
            self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
            self.canvas.create_image(0, 0, anchor=NW, image=self.img_tk)

        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            Label(self.window, text="[Falta Imagen]", bg="white", fg="gray").place(x=50, y=50)

        # Cargar y mostrar imagen de usuario
        self.usuario_img = Image.open("login/images/usuario.png")
        self.usuario_img_resized = self.usuario_img.resize((100, 100))
        self.usuario_img_tk = ImageTk.PhotoImage(self.usuario_img_resized)
        self.canvas.create_image(200, 150, anchor=CENTER, image=self.usuario_img_tk)

        # Crear campos de texto y entradas para "Usuario" y "Contraseña"
        self.canvas.create_text(200, 265, text="Usuario", font=('Arial', 14), fill="white")
        self.username_entry = Entry(self.window, font=('Arial', 14), fg="black", bg=self.window["bg"], bd=0, highlightthickness=2, highlightbackground="white", insertbackground="white", justify='left', relief="flat")
        self.username_entry.place(x=70, y=285, width=220, height=30)
        self.username_entry.config(borderwidth=2, relief="solid")

        # Icono de usuario
        self.user_icon_img = Image.open("login/images/usuario.png")
        self.user_icon_img_resized = self.user_icon_img.resize((30, 30))
        self.user_icon_tk = ImageTk.PhotoImage(self.user_icon_img_resized)
        self.canvas.create_image(325, 300, image=self.user_icon_tk)

        # Campo de texto para "Contraseña"
        self.canvas.create_text(200, 370, text="Contraseña", font=('Arial', 14), fill="white")
        self.password_entry = Entry(self.window, font=('Arial', 14), fg="black", bg=self.window["bg"], bd=0, highlightthickness=2, highlightbackground="white", insertbackground="white", show="*", justify='left', relief="flat")
        self.password_entry.place(x=70, y=390, width=220, height=30)
        self.password_entry.config(borderwidth=2, relief="solid")

        # Icono de candado
        self.pass_icon_img = Image.open("login/images/candado.png")
        self.pass_icon_img_resized = self.pass_icon_img.resize((45, 45))
        self.pass_icon_tk = ImageTk.PhotoImage(self.pass_icon_img_resized)
        self.canvas.create_image(325, 400, image=self.pass_icon_tk)

        # Botón de inicio de sesión
        self.login_button = Button(self.window, text="Iniciar Sesión", font=('Arial', 14), fg="white", bg="#4CAF50", activebackground="#45a049", bd=0, command=self.iniciar_sesion)
        self.login_button.place(x=100, y=450, width=220, height=40)

        # Variable para el texto de error (inicialmente vacío)
        self.error_text = None

    def iniciar_sesion(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.error_text:
            self.canvas.delete(self.error_text)

        if validar_login(username, password):  # Validar credenciales
            if self.on_success_callback:
                self.on_success_callback()
            self.error_text = None  # Limpiar error si es válido
        else:
            self.error_text = self.canvas.create_text(210, 510, text="Usuario o contraseña incorrectos", font=('Arial', 12), fill="red")  # Mostrar error
