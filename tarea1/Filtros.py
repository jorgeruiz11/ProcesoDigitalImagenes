from tkinter import filedialog, simpledialog, messagebox
from ManejadorImagen import ManejadorImagen
from ManejadorImagen import *
from PIL import ImageTk, Image
import tkinter as tk
import cv2
import os

class Filtros(object):

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aplicador de Filtros")
        self.ventana.geometry("1000x550")
        self.ventana.configure(bg='white')

        self.ListaFiltros = ["Escala de Grises", "Brillo", "Mosaico"]

        self.grises = [
        "Gris 1", "Gris 2", "Gris 3", "Gris 4", "Gris 5",
        "Gris 6", "Gris 7", "Gris 8", "Gris 9"]

        # Ejecución principal de los menús
        menu_p = self.barra_menu_principal()
        filtros = self.menu_filtros_desplegable(menu_p)
        self.menu_desplegable_grises(filtros)


    """ Seccion de Filtros """

    # Filtro escala de grises tipo 1
    def tipo_gris1(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(1)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 2
    def tipo_gris2(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(2)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 3
    def tipo_gris3(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(3)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 4
    def tipo_gris4(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(4)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 5
    def tipo_gris5(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(5)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 6
    def tipo_gris6(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(6)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 7
    def tipo_gris7(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(7)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 8
    def tipo_gris8(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(8)
        self.escala_gris(img_filtrada)

    # Filtro escala de grises tipo 9
    def tipo_gris9(self):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).escala_grises(9)
        self.escala_gris(img_filtrada)

    # Llama al método encargado de cargar la imagen en pantalla
    def escala_gris(self, img_filtrada):
        self.carga_imagen_filtrada(img_filtrada)

     # Aplica el filtro de brillo a la imagen y manda a llamar al método
     # encargado de mostrarlo en pantalla
    def fbrillo(self, b1,g1,r1):
        # img_filtrada = ManejadorImagen(self.intro_ruta.get()).brillo((20,20,20))
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).brillo(b1,g1,r1)
        self.carga_imagen_filtrada(img_filtrada)

     # Aplica el filtro de mosaico a la imagen y manda a llamar al método
     # encargado de mostrarlo en pantalla
    def fmosaico(self, size):
        # reg = ManejadorImagen(self.intro_ruta.get()).calcula_regiones((20,20))
        reg = ManejadorImagen(self.intro_ruta.get()).calcula_regiones((size[0],size[1]))
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).mosaico(reg)
        self.carga_imagen_filtrada(img_filtrada)


    def carga_imagen_filtrada(self, img_filtrada):
        ruta_img = guarda_resultado("filtrada.jpeg", img_filtrada)
        img = Image.open(ruta_img)
        borra_resultado(ruta_img)
        img_rsize = img.resize((400,400))
        imagen = ImageTk.PhotoImage(img_rsize)
        imagen.image = imagen

        panel = tk.Label(self.ventana, image = imagen).place(x=525,y=75)


    def carga_imagen_original(self, ruta_img):
        if not os.path.exists(ruta_img):
            messagebox.showwarning('Error', 'El archivo no existe o no es la ruta correcta.')

        img_original = img = Image.open(ruta_img)
        img_rsize = img.resize((400,400))
        imagen = ImageTk.PhotoImage(img_rsize)
        imagen.image = imagen

        panel = tk.Label(self.ventana, image = imagen).place(x=75,y=75)


    # Crea la barra del menú principal y el boton principal para cargar la imagen1
    # Tambien nos sirve como base para que el siguiente menú los reciba como argumento
    # Y Nos permita crear los menús desplegables
    def barra_menu_principal(self):
        barra_menu_p = tk.Menu(self.ventana)
        # barra_menu_p.add_command(label='Cargar Imagen', command=self.carga_imagen_original)
        barra_menu_p.add_command(label='Cargar Imagen', command=self.ventana_img_original)
        return barra_menu_p

    # Coloca el menú desplegable de los tipos de filtros disponibles
    # Hasta ahora el menú se despliega en 3 tipos de filtros
    def menu_filtros_desplegable(self, barra_menu_p):
        desplegable = tk.Menu(barra_menu_p, tearoff=0)
        # desplegable.add_command(label=self.ListaFiltros[2], command=self.fmosaico)
        desplegable.add_command(label=self.ListaFiltros[1], command=self.ventana_brillo)
        desplegable.add_command(label=self.ListaFiltros[2], command=self.ventana_mosaico)
        barra_menu_p.add_cascade(label='Filtros', menu=desplegable)

        self.ventana.config(menu=barra_menu_p)
        return desplegable

    # Coloca el menú desplegable de los tipos de gris en la escala de grises
    # El menu de escala de grises despliega 9 tipos de grises
    def menu_desplegable_grises(self, menu_filtros_desplegable):
        gris_desp = tk.Menu(menu_filtros_desplegable, tearoff=0)
        gris_desp.add_command(label=self.grises[0], command=self.tipo_gris1)
        gris_desp.add_command(label=self.grises[1], command=self.tipo_gris2)
        gris_desp.add_command(label=self.grises[2], command=self.tipo_gris3)
        gris_desp.add_command(label=self.grises[3], command=self.tipo_gris4)
        gris_desp.add_command(label=self.grises[4], command=self.tipo_gris5)
        gris_desp.add_command(label=self.grises[5], command=self.tipo_gris6)
        gris_desp.add_command(label=self.grises[6], command=self.tipo_gris7)
        gris_desp.add_command(label=self.grises[7], command=self.tipo_gris8)
        gris_desp.add_command(label=self.grises[8], command=self.tipo_gris9)
        menu_filtros_desplegable.add_cascade(label='Escala de Grises', menu=gris_desp)

    # Leemos la entrada del brillo del usuario
    def ventana_brillo(self):
        v_brillo = tk.Toplevel()
        v_brillo.geometry("200x150")
        v_brillo.title("Cantidad de brillo por componente")

        # Entrada para texto en blue
        azul = tk.Label(v_brillo, text="Azul:")
        azul.grid(pady=4, row=0, column=0)
        intro_brillo_b = tk.IntVar()
        cuadro_texto_b = tk.Entry(v_brillo, textvariable=intro_brillo_b)
        cuadro_texto_b.place(x=50, y=5)

        # Entrada para texto en green
        verde = tk.Label(v_brillo, text="Verde:")
        verde.grid(pady=4, row=1, column=0)
        intro_brillo_g = tk.IntVar()
        cuadro_texto_g = tk.Entry(v_brillo, textvariable=intro_brillo_g)
        cuadro_texto_g.place(x=50, y=30)

        # Entrada para texto en red
        rojo = tk.Label(v_brillo, text="Rojo:")
        rojo.grid(pady=4, row=2, column=0)
        intro_brillo_r = tk.IntVar()
        cuadro_texto_r = tk.Entry(v_brillo, textvariable=intro_brillo_r)
        cuadro_texto_r.place(x=50, y=55)

        # Botón para confirmar el brillo
        b_listo = tk.Button(v_brillo, text="Listo",
        command= lambda: self.fbrillo(intro_brillo_b.get(),intro_brillo_g.get(),intro_brillo_r.get()))
        b_listo.grid(row=4, column=2)

        v_brillo.mainloop()

    # Leemos la entrada del pixelado del usuario
    def ventana_mosaico(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("200x120")
        v_mosaico.title("Tamaño del pixelado")

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.grid(pady=4, row=0, column=0)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=50, y=5)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.grid(pady=4, row=1, column=0)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=50, y=30)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico((intro_x.get(),intro_y.get())))
        b_listo.grid(row=4, column=2)

        v_mosaico.mainloop()

    def ventana_img_original(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("250x100")
        v_mosaico.title("Tamaño del pixelado")

        # Entrada para texto en eje X
        ruta = tk.Label(v_mosaico, text="Ruta o Nombre:")
        ruta.grid(pady=5, row=0, column=0)
        self.intro_ruta = tk.StringVar()
        text_ruta = tk.Entry(v_mosaico, textvariable=self.intro_ruta)
        text_ruta.place(x=100, y=5)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.carga_imagen_original(self.intro_ruta.get()))
        b_listo.grid(row=4, column=2)

    # Se encarga de mantener la ventana abierta
    def main_lp(self):
        self.ventana.mainloop()


# Arranque
if __name__ == '__main__':
    f = Filtros()
    f.main_lp()
