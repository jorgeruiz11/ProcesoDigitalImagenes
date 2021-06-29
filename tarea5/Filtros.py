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
        self.ventana.geometry("1200x600")
        self.ventana.configure(bg='white')

        self.imagen_s = None

        self.ListaFiltros = ["Recursivas Escala de Grises", 'Recursivas a Color']

        # Ejecución principal de los menús
        menu_p = self.barra_menu_principal()


    def frecursivas_bw(self, sizeX, sizeY):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).gen_gray_images( (sizeX,sizeY) )
        self.carga_imagen_filtrada(img_filtrada)

        self.imagen_s = img_filtrada

        return self.imagen_s

    def frecursivas_c(self, sizeX, sizeY):
        img_filtrada = ManejadorImagen(self.intro_ruta.get()).gen_color_images( (sizeX,sizeY) )
        self.carga_imagen_filtrada(img_filtrada)

        self.imagen_s = img_filtrada

        return self.imagen_s


    def carga_imagen_filtrada(self, img_filtrada):
        imagen = ImageTk.PhotoImage(img_filtrada)
        imagen.image = imagen

        panel = tk.Label(self.ventana, image = imagen).place(x=625,y=75)

    def carga_imagen_original(self, ruta_img):
        if not os.path.exists(ruta_img):
            messagebox.showwarning('Error', 'El archivo no existe o no es la ruta correcta.')

        img = Image.open(ruta_img)
        img_rsize = img.resize((500,400))
        imagen = ImageTk.PhotoImage(img_rsize)
        imagen.image = imagen

        panel = tk.Label(self.ventana, image = imagen).place(x=75,y=75)

        self.imagen_s = img_rsize

        return self.imagen_s

    def guarda_imagen(self, titulo):
        if not self.imagen_s:
            messagebox.showwarning('Error', 'No hay imagen para guardar.')
            return

        img_filtrada = self.imagen_s
        img_filtrada.save(titulo)
        messagebox.showinfo('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')


    # Crea la barra del menú principal y el boton principal para cargar la imagen
    def barra_menu_principal(self):
        barra_menu_p = tk.Menu(self.ventana)
        barra_menu_p.add_command(label='Cargar Imagen', command=self.ventana_img_original)
        barra_menu_p.add_command(label=self.ListaFiltros[0], command=self.ventana_R_BW)
        barra_menu_p.add_command(label=self.ListaFiltros[1], command=self.ventana_R_C)
        barra_menu_p.add_command(label='Guardar Imagen', command=self.ventana_guardar)

        tk.Label(None, text="El tamaño de las imagenes es de 500x400", fg="firebrick").pack()

        self.ventana.config(menu=barra_menu_p)

        return barra_menu_p


    def ventana_guardar(self):
        v_guardar = tk.Toplevel()
        v_guardar.geometry("400x100")
        v_guardar.title("Guardar")

        # Entrada para guardar
        guardar = tk.Label(v_guardar, text="Nombre (con extension):")
        guardar.grid(pady=4, row=0, column=0)
        intro_guardar = tk.StringVar()
        cuadro_guardar = tk.Entry(v_guardar, textvariable=intro_guardar, width=20)
        cuadro_guardar.place(x=180, y=5)

        # Botón para confirmar
        b_listo = tk.Button(v_guardar, text="Listo",
        command= lambda: self.guarda_imagen(intro_guardar.get()))
        b_listo.place(x=160, y=50)

        v_guardar.mainloop()

    def ventana_R_BW(self):
        v_r_BW = tk.Toplevel()
        v_r_BW.geometry("350x120")
        v_r_BW.title("Datos")

        # Entrada para transparencia
        pixelado_bw_X = tk.Label(v_r_BW, text="Tamaño del pixelado en X:")
        pixelado_bw_X.grid(pady=4, row=1, column=0)
        intro_pixelado_bw_X = tk.IntVar()
        cadro_pixelado_bw_X = tk.Entry(v_r_BW, textvariable=intro_pixelado_bw_X)
        cadro_pixelado_bw_X.place(x=180, y=5)

        # Entrada para transparencia
        pixelado_bw_Y = tk.Label(v_r_BW, text="Tamaño del pixelado en Y:")
        pixelado_bw_Y.grid(pady=5, row=2, column=0)
        intro_pixelado_bw_Y = tk.IntVar()
        cadro_pixelado_bw_Y = tk.Entry(v_r_BW, textvariable=intro_pixelado_bw_Y)
        cadro_pixelado_bw_Y.place(x=180, y=35)

        # Botón para confirmar
        b_listo = tk.Button(v_r_BW, text="Listo",
        command= lambda: self.frecursivas_bw( intro_pixelado_bw_X.get(), intro_pixelado_bw_Y.get()))
        b_listo.place(x=120, y=70)

        v_r_BW.mainloop()

    def ventana_R_C(self):
        v_r_C = tk.Toplevel()
        v_r_C.geometry("350x120")
        v_r_C.title("Datos")

        # Entrada para transparencia
        pixelado_c_X = tk.Label(v_r_C, text="Tamaño del pixelado en X:")
        pixelado_c_X.grid(pady=4, row=1, column=0)
        intro_pixelado_c_X = tk.IntVar()
        cadro_pixelado_c_X = tk.Entry(v_r_C, textvariable=intro_pixelado_c_X)
        cadro_pixelado_c_X.place(x=180, y=5)

        # Entrada para transparencia
        pixelado_c_Y = tk.Label(v_r_C, text="Tamaño del pixelado en Y:")
        pixelado_c_Y.grid(pady=5, row=2, column=0)
        intro_pixelado_c_Y = tk.IntVar()
        cadro_pixelado_c_Y = tk.Entry(v_r_C, textvariable=intro_pixelado_c_Y)
        cadro_pixelado_c_Y.place(x=180, y=35)

        # Botón para confirmar
        b_listo = tk.Button(v_r_C, text="Listo",
        command= lambda: self.frecursivas_c( intro_pixelado_c_X.get(), intro_pixelado_c_Y.get()))
        b_listo.place(x=120, y=70)

        v_r_C.mainloop()


    def ventana_img_original(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("450x100")
        v_mosaico.title("Ruta | Nombre imagen")

        # Entrada para texto en eje X
        ruta = tk.Label(v_mosaico, text="Ruta o Nombre:")
        ruta.grid(pady=5, row=0, column=0)
        self.intro_ruta = tk.StringVar()
        text_ruta = tk.Entry(v_mosaico, textvariable=self.intro_ruta, width=40)
        text_ruta.place(x=110, y=5)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.carga_imagen_original(self.intro_ruta.get()))
        b_listo.place(x=200, y=45)


    # Se encarga de mantener la ventana abierta
    def main_lp(self):
        self.ventana.mainloop()


# Arranque
if __name__ == '__main__':
    f = Filtros()
    f.main_lp()
