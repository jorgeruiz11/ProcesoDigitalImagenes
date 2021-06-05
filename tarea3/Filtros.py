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
        self.ventana.geometry("600x550")
        self.ventana.configure(bg='white')

        self.filtros = [
        "M en Colores", "M en Tonos de Gris", "Letras que Simulan tonos de Gris",
        "Letras en Colores", "Letras en Tonos de Gris", "Texto en colores",
        "Dominós Blancos", "Dominós Negros", "Naipes"]

        # Ejecución principal de los menús
        menu_p = self.barra_menu_principal()
        filtros = self.menu_filtros_desplegable(menu_p)


    """ Seccion de Filtros """

    
    def fmosaico_color(self, size, titulo, font_size):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).mosaico_color(l_coords, size, titulo, font_size)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fmosaico_gris(self, size, titulo, font_size):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).mosaico_gris(l_coords, titulo, font_size)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fmosaico_simbolosBW(self, size, titulo, font_size):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).mosaico_simbolosBW(l_coords, titulo, font_size)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fmosaico_simbolosC(self, size, titulo, font_size):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).mosaico_simbolosC(l_coords, size, titulo, font_size)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fmosaico_texto(self, size, titulo, font_size, texto):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).mosaico_texto(l_coords, size, titulo, font_size, texto)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fmosaico_simbolos_BW_tonos(self, size, titulo, font_size):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).mosaico_simbolos_BW_tonos(l_coords, titulo, font_size)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fcartas(self, size, titulo):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).cartas(l_coords, titulo)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fdomino_blanco(self, size, titulo):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).domino_blanco(l_coords, titulo)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')

    
    def fdomino_negro(self, size, titulo):
        l_coords = ManejadorImagen(self.intro_ruta.get()).cuadricula((size[0],size[1]))
        ManejadorImagen(self.intro_ruta.get()).domino_negro(l_coords, titulo)
        messagebox.showwarning('Terminado', 'Archivo guardado como: ' + titulo + '\n\n' + 'Si el archivo ya existía se sobreescribió.')



    def carga_imagen_original(self, ruta_img):
        if not os.path.exists(ruta_img):
            messagebox.showwarning('Error', 'El archivo no existe o la ruta es incorrecta.')

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
        barra_menu_p.add_command(label='Cargar Imagen', command=self.ventana_img_original)
        return barra_menu_p

    # Coloca el menú desplegable de los tipos de filtros disponibles
    def menu_filtros_desplegable(self, barra_menu_p):
        filtros_deps = tk.Menu(barra_menu_p, tearoff=0)
        
        filtros_deps.add_command(label=self.filtros[0], command=self.ventana_mosaico_color)
        filtros_deps.add_command(label=self.filtros[1], command=self.ventana_mosaico_gris)
        filtros_deps.add_command(label=self.filtros[2], command=self.ventana_mosaico_simbolosBW)
        filtros_deps.add_command(label=self.filtros[3], command=self.ventana_mosaico_simbolosC)
        filtros_deps.add_command(label=self.filtros[4], command=self.ventana_mosaico_simbolos_BW_tonos)
        filtros_deps.add_command(label=self.filtros[5], command=self.ventana_mosaico_texto)
        filtros_deps.add_command(label=self.filtros[6], command=self.ventana_mosaico_domino_blanco)
        filtros_deps.add_command(label=self.filtros[7], command=self.ventana_mosaico_domino_negro)
        filtros_deps.add_command(label=self.filtros[8], command=self.ventana_mosaico_cartas)
        barra_menu_p.add_cascade(label='Filtros', menu=filtros_deps)

        self.ventana.config(menu=barra_menu_p)
        return filtros_deps



    def ventana_mosaico_color(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")


        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        font_size = tk.Label(v_mosaico, text="Tamaño letra (HTML):")
        font_size.place(x=0, y=35)
        intro_font_size = tk.StringVar()
        text_font_size = tk.Entry(v_mosaico, textvariable=intro_font_size, width=20)
        text_font_size.place(x=150, y=35)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=65)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=65)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=95)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=95)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico_color( (intro_x.get(),intro_y.get()), intro_guardado.get(), intro_font_size.get() ))
        b_listo.place(x=110, y=125)

        v_mosaico.mainloop()


    def ventana_mosaico_gris(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        font_size = tk.Label(v_mosaico, text="Tamaño letra (HTML):")
        font_size.place(x=0, y=35)
        intro_font_size = tk.StringVar()
        text_font_size = tk.Entry(v_mosaico, textvariable=intro_font_size, width=20)
        text_font_size.place(x=150, y=35)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=65)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=65)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=95)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=95)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico_gris( (intro_x.get(),intro_y.get()), intro_guardado.get(), intro_font_size.get() ))
        b_listo.place(x=110, y=125)

        v_mosaico.mainloop()


    def ventana_mosaico_simbolosBW(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        font_size = tk.Label(v_mosaico, text="Tamaño letra (HTML):")
        font_size.place(x=0, y=35)
        intro_font_size = tk.StringVar()
        text_font_size = tk.Entry(v_mosaico, textvariable=intro_font_size, width=20)
        text_font_size.place(x=150, y=35)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=65)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=65)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=95)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=95)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico_simbolosBW( (intro_x.get(),intro_y.get()), intro_guardado.get(), intro_font_size.get() ))
        b_listo.place(x=110, y=125)

        v_mosaico.mainloop()


    def ventana_mosaico_simbolosC(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        font_size = tk.Label(v_mosaico, text="Tamaño letra (HTML):")
        font_size.place(x=0, y=35)
        intro_font_size = tk.StringVar()
        text_font_size = tk.Entry(v_mosaico, textvariable=intro_font_size, width=20)
        text_font_size.place(x=150, y=35)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=65)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=65)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=95)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=95)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico_simbolosC( (intro_x.get(),intro_y.get()), intro_guardado.get(), intro_font_size.get() ))
        b_listo.place(x=110, y=125)

        v_mosaico.mainloop()



    def ventana_mosaico_simbolos_BW_tonos(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        font_size = tk.Label(v_mosaico, text="Tamaño letra (HTML):")
        font_size.place(x=0, y=35)
        intro_font_size = tk.StringVar()
        text_font_size = tk.Entry(v_mosaico, textvariable=intro_font_size, width=20)
        text_font_size.place(x=150, y=35)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=65)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=65)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=95)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=95)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico_simbolos_BW_tonos( (intro_x.get(),intro_y.get()), intro_guardado.get(), intro_font_size.get() ))
        b_listo.place(x=110, y=125)

        v_mosaico.mainloop()



    def ventana_mosaico_texto(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("620x350")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        font_size = tk.Label(v_mosaico, text="Tamaño letra (HTML):")
        font_size.place(x=0, y=35)
        intro_font_size = tk.StringVar()
        text_font_size = tk.Entry(v_mosaico, textvariable=intro_font_size, width=20)
        text_font_size.place(x=150, y=35)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=65)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=65)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=95)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=95)

        texto_contenido = tk.Label(v_mosaico, text="Texto:")
        texto_contenido.place(x=0, y=125)
        intro_texto_contenido = tk.StringVar()
        text_texto_contenido = tk.Entry(v_mosaico, textvariable=intro_texto_contenido, width=70)
        text_texto_contenido.place(x=45, y=125, height=150)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fmosaico_texto( (intro_x.get(),intro_y.get()), intro_guardado.get(), intro_font_size.get(), intro_texto_contenido.get() ))
        b_listo.place(x=225, y=300)

        v_mosaico.mainloop()



    def ventana_mosaico_cartas(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=35)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=35)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=65)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=65)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fcartas( (intro_x.get(),intro_y.get()), intro_guardado.get() ))
        b_listo.place(x=110, y=100)

        v_mosaico.mainloop()



    def ventana_mosaico_domino_blanco(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=35)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=35)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=65)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=65)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fdomino_blanco( (intro_x.get(),intro_y.get()), intro_guardado.get() ))
        b_listo.place(x=110, y=100)

        v_mosaico.mainloop()



    def ventana_mosaico_domino_negro(self):
        v_mosaico = tk.Toplevel()
        v_mosaico.geometry("500x200")
        v_mosaico.title("Datos")

        guardado = tk.Label(v_mosaico, text="Guardar como:")
        guardado.place(x=0, y=5)
        intro_guardado = tk.StringVar()
        text_guardado = tk.Entry(v_mosaico, textvariable=intro_guardado, width=30)
        text_guardado.place(x=110, y=5)

        # Entrada para texto en eje X
        ejex = tk.Label(v_mosaico, text="Eje X:")
        ejex.place(x=0, y=35)
        intro_x = tk.IntVar()
        text_x = tk.Entry(v_mosaico, textvariable=intro_x)
        text_x.place(x=45, y=35)

        # Entrada para texto en eje Y
        ejey = tk.Label(v_mosaico, text="Eje Y:")
        ejey.place(x=0, y=65)
        intro_y = tk.IntVar()
        text_y = tk.Entry(v_mosaico, textvariable=intro_y)
        text_y.place(x=45, y=65)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_mosaico, text="Listo",
        command= lambda: self.fdomino_negro( (intro_x.get(),intro_y.get()), intro_guardado.get() ))
        b_listo.place(x=110, y=100)

        v_mosaico.mainloop()




    def ventana_img_original(self):
        v_igm_orig = tk.Toplevel()
        v_igm_orig.geometry("450x100")
        v_igm_orig.title("Ruta | Nombre imagen")

        # Entrada para texto en eje X
        ruta = tk.Label(v_igm_orig, text="Ruta o Nombre:")
        ruta.grid(pady=5, row=0, column=0)
        self.intro_ruta = tk.StringVar()
        text_ruta = tk.Entry(v_igm_orig, textvariable=self.intro_ruta, width=40)
        text_ruta.place(x=110, y=5)

        # Botón para confirmar el pixelado
        b_listo = tk.Button(v_igm_orig, text="Listo",
        command= lambda: self.carga_imagen_original(self.intro_ruta.get()), width=10)
        b_listo.place(x=110, y=50)


    # Se encarga de mantener la ventana abierta
    def main_lp(self):
        self.ventana.mainloop()


# Arranque
if __name__ == '__main__':
    f = Filtros()
    f.main_lp()
