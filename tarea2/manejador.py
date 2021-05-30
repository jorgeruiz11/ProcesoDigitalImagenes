import cv2
import numpy as np
from PIL import Image
from os import remove
from os import path

np.seterr(over='ignore')

# Método que usaremos para mostrar la imagen resultante de aplicar el filtro
def muestra_resultado(imagen):
    cv2.imshow('Practica 2', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def guarda_resultado(titulo, imagen):
    cv2.imwrite(titulo, imagen)
    return titulo

def borra_resultado(titulo):
    if path.exists(titulo):
        remove(titulo)

class manejador(object):

    def __init__(self, ruta_imagen):
        self.imagen1 = cv2.imread(ruta_imagen)
        wancho, halto, c = self.imagen1.shape

        # Si la imagen es mas grande que 800x800, 800x_, _x800 la hacemos pequeña
        if wancho > 800 or halto > 800:
            width = int(self.imagen1.shape[1] * 20 / 100)
            height = int(self.imagen1.shape[0] * 20 / 100)
            dim = (width, height)

            self.imagen = cv2.resize(self.imagen1, dim)
            self.ancho, self.alto, c = self.imagen.shape
        else:
            self.imagen = self.imagen1
            self.ancho, self.alto, c = self.imagen1.shape


    # Lo usaremos para verificar que cualquier valor en la entrada de un
    # pixel no esté fuera del rango [0,255]
    def verificador(self, componente, valor):
        suma = componente + valor
        if suma > 255:
            return 255
        elif suma < 0:
            return 0
        else:
            return suma

    # Lo usaremos para verificar que cualquier valor en la entrada de un
    # pixel no esté fuera del rango [0,255]
    def verif_and(self, componente, valor):
        suma = componente & valor
        if suma > 255:
            return 255
        elif suma < 0:
            return 0
        else:
            return suma

    # Ejercicio 1
    def alto_contraste(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = map(int, self.imagen[x,y])
                color_contraste = round((b + g + r) / 3)

                if color_contraste > 127:
                    color_contraste = 255
                else:
                    color_contraste = 0

                self.imagen.itemset((x,y,0), color_contraste) # blue
                self.imagen.itemset((x,y,1), color_contraste) # green
                self.imagen.itemset((x,y,2), color_contraste) # red

        return self.imagen

    # Ejercicio 2
    def inverso(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = map(int, self.imagen[x,y])
                color_contraste = round((b + g + r) / 3)

                if color_contraste > 127:
                    color_contraste = 0
                else:
                    color_contraste = 255

                self.imagen.itemset((x,y,0), color_contraste) # blue
                self.imagen.itemset((x,y,1), color_contraste) # green
                self.imagen.itemset((x,y,2), color_contraste) # red

        return self.imagen


    # Ejercicio 3
    # Cada número de entrada es como el porcentaje que lleva.
    # (200,150,80) define el porcentaje de cada uno (b,g,r)
    def rgb(self, bin, gin, rin):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = self.imagen[x,y]

                # b = b & bin
                # g = g & bin
                # r = r & bin

                b = self.verif_and(b, bin)
                g = self.verif_and(g, bin)
                r = self.verif_and(r, bin)

                self.imagen.itemset((x,y,0), b) # blue
                self.imagen.itemset((x,y,1), g) # green
                self.imagen.itemset((x,y,2), r) # red

        return self.imagen
