import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from manejador import manejador_img
from manejador import *
import os

class filtros(object):

    def __init__(self):
        self.canvas = tk.Tk()
        self.canvas.title('PDI | Filtros')
        self.canvas.geometry('1000x550')
        self.canvas.configure(bg='white')
        self.menu = tk.Menu(self.canvas)
        self.canvas.config(menu=self.menu)
        self.subMenu()

    def altocontraste(self):
        img_f = manejador_img(self.intro_ruta.get()).alto_contraste()
        self.carga_imagen_f(img_f)

    def finverso(self):
        img_f = manejador_img(self.intro_ruta.get()).inverso()
        self.carga_imagen_f(img_f)

    def fRGB(self, bin, gin, rin):
        img_f = manejador_img(self.intro_ruta.get()).rgb(bin,gin,rin)
        self.carga_imagen_f(img_f)

    def subMenu(self):
        subMenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=subMenu)
        subMenu.add_command(label="Cargar imagen", command=self.ventana_orig)
        subMenu.add_separator()
        subMenu.add_command(label="Salir", command=self.doN)

        menuFiltros=tk.Menu(self.menu)
        self.menu.add_cascade(label="Filtros", menu=menuFiltros)
        menuFiltros.add_command(label="Alto contraste", command=self.altocontraste)
        menuFiltros.add_command(label="Inverso", command=self.finverso)
        menuFiltros.add_command(label="RGB", command=self.v_rgb)
        subMenu.add_separator()

        menu_convolucion = tk.Menu(menuFiltros)
        menuFiltros.add_cascade(label="Convolucion", menu=menu_convolucion)
        menu_convolucion.add_command(label="Hola")


    def carga_imagen_o(self, ruta):
        if not os.path.exists(ruta):
            messagebox.showwarning('Error', 'No existe el archivo o la ruta especificada es incorrecta')

        img = Image.open(ruta)
        img_rsize = img.resize((400,400))
        imagen = ImageTk.PhotoImage(img_rsize)
        imagen.image = imagen # sin esto no muestra la imagen

        c_img = tk.Label(self.canvas, image=imagen).place(x=75, y=75)

    def carga_imagen_f(self, img_original):
        ruta_img = guarda_resultado("filtrada.jpeg", img_original)
        img = Image.open(ruta_img)
        borra_resultado(ruta_img)
        img_rsize = img.resize((400,400))
        imagen = ImageTk.PhotoImage(img_rsize)
        imagen.image = imagen

        c_img = tk.Label(self.canvas, image = imagen).place(x=525,y=75)

    def ventana_orig(self):
        v_orig = tk.Toplevel()
        v_orig.geometry("250x100")
        v_orig.title("Ruta | Nombre imagen")

        ruta = tk.Label(v_orig, text="Ruta o Nombre:")
        ruta.grid(pady=5, row=0, column=0)
        self.intro_ruta = tk.StringVar()
        text_ruta = tk.Entry(v_orig, textvariable=self.intro_ruta)
        text_ruta.place(x=100, y=5)

        b_listo = tk.Button(v_orig, text="Listo",
        command= lambda: self.carga_imagen_o(self.intro_ruta.get()))
        b_listo.grid(row=4, column=2)

    def v_rgb(self):
        v_bgr = tk.Toplevel()
        v_bgr.geometry("200x150")
        v_bgr.title("Cantidad de color por componente")

        # Entrada para texto en blue
        azul = tk.Label(v_bgr, text="Azul:")
        azul.grid(pady=4, row=0, column=0)
        intro_rgb_b = tk.IntVar()
        cuadro_texto_b = tk.Entry(v_bgr, textvariable=intro_rgb_b)
        cuadro_texto_b.place(x=50, y=5)

        # Entrada para texto en green
        verde = tk.Label(v_bgr, text="Verde:")
        verde.grid(pady=4, row=1, column=0)
        intro_rgb_g = tk.IntVar()
        cuadro_texto_g = tk.Entry(v_bgr, textvariable=intro_rgb_g)
        cuadro_texto_g.place(x=50, y=30)

        # Entrada para texto en red
        rojo = tk.Label(v_bgr, text="Rojo:")
        rojo.grid(pady=4, row=2, column=0)
        intro_rgb_r = tk.IntVar()
        cuadro_texto_r = tk.Entry(v_bgr, textvariable=intro_rgb_r)
        cuadro_texto_r.place(x=50, y=55)

        # Botón para confirmar el rgb
        b_listo = tk.Button(v_bgr, text="Listo",
        command= lambda: self.fRGB(intro_rgb_b.get(),intro_rgb_g.get(),intro_rgb_r.get()))
        b_listo.grid(row=4, column=2)

        v_bgr.mainloop()


    def doN(self):
        print("DO SOMTHING USEFULL... please")

    def mainlp(self):
        self.canvas.mainloop()

f = filtros()
f.mainlp()
