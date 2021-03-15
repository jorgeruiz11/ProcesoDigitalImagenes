import cv2
import numpy as np
from PIL import Image
from os import remove
from os import path

np.seterr(over='ignore')

# Método que usaremos para mostrar la imagen resultante de aplicar el filtro
def muestra_resultado(imagen):
    cv2.imshow('Practica 1', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def guarda_resultado(titulo, imagen):
    cv2.imwrite(titulo, imagen)
    return titulo

def borra_resultado(titulo):
    if path.exists(titulo):
        remove(titulo)

class ManejadorImagen(object):

    def __init__(self, ruta_imagen):
        self.imagen1 = cv2.imread(ruta_imagen)

        scale_percent = 20 # percent of original size
        width = int(self.imagen1.shape[1] * scale_percent / 100)
        height = int(self.imagen1.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        self.imagen = cv2.resize(self.imagen1, dim)
        self.ancho, self.alto, c = self.imagen.shape # shape nos da las dimensiones de la matriz

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

    # Ejercicios 1,2,3,4,5,6,7,8,9
    def escala_grises(self, id):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = self.imagen[x,y]

                if id == 1:
                    gris = round((r+g+b)/3)
                elif id == 2:
                    gris = round((r*0.3 + g*0.59 + b*0.11))
                elif id == 3:
                    gris = round((r*0.2126 + g*0.7152 + b*0.0722))
                elif id == 4:
                    gris = round(max(r,g,b) + min(r,g,b) / 2)
                elif id == 5:
                    gris = round(max(r,g,b))
                elif id == 6:
                    gris = round(min(r,g,b))
                elif id == 7:
                    gris = r
                elif id == 8:
                    gris = g
                elif id == 9:
                    gris = b

                self.imagen.itemset((x,y,0), gris) # blue
                self.imagen.itemset((x,y,1), gris) # green
                self.imagen.itemset((x,y,2), gris) # red

        return self.imagen

    # Ejercicio 10
    def brillo(self, b1,g1,r1):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = self.imagen[x,y]

                self.imagen.itemset((x,y,0), self.verificador(b,b1)) # blue
                self.imagen.itemset((x,y,1), self.verificador(g,g1)) # green
                self.imagen.itemset((x,y,2), self.verificador(r,r1)) # red

        return self.imagen


    # Ejercicio 12
    def azul(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = self.imagen[x,y]

                self.imagen.itemset((x,y,0), b) # blue
                self.imagen.itemset((x,y,1), 0) # green
                self.imagen.itemset((x,y,2), 0) # red

        return self.imagen

    # Ejercicio 13
    def verde(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = self.imagen[x,y]

                self.imagen.itemset((x,y,0), 0) # blue
                self.imagen.itemset((x,y,1), g) # green
                self.imagen.itemset((x,y,2), 0) # red

        return self.imagen


    # Ejercicio 14
    def rojo(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                b,g,r = self.imagen[x,y]

                self.imagen.itemset((x,y,0), 0) # blue
                self.imagen.itemset((x,y,1), 0) # green
                self.imagen.itemset((x,y,2), r) # red

        return self.imagen

    # Cada region consta podemos verla como sus 4 esquinas
    # Ej: En la region de 20x25 tendriamos:
    # xizq = 0, xder = 20, yizq = 0, yder = 25 -> todos juntos nos dan region_1
    def calcula_regiones(self, size):
        x, y = size[0], size[1]
        l_coordenadas = []
        xIzq = 0
        xDer = x

        while xDer < self.ancho:
            yIzq = 0
            yDer = y
            while yDer < self.alto:
                l_coordenadas.append((xIzq,yIzq,xDer,yDer))
                yIzq = yDer
                yDer += y

            yDer = self.alto - 1
            l_coordenadas.append((xIzq,yIzq,xDer,yDer))
            xIzq = xDer
            xDer += x

        xDer = self.ancho - 1
        yIzq = 0
        yDer = y

        while yDer < self.ancho:
            l_coordenadas.append((xIzq,yIzq,xDer,yDer))
            yIzq = yDer
            yDer += y

        yDer = self.alto
        l_coordenadas.append((xIzq,yIzq,xDer,yDer))

        return l_coordenadas


    # Ejercicio 11
    def mosaico(self, l_coordenadas):
        bgrImg = self.imagen
        pixeles = self.imagen

        for (xIzq,yIzq,xDer,yDer) in l_coordenadas:
            b_prom, g_prom, r_prom = 0,0,0
            total = 1

            for x in range(xIzq,xDer):
                for y in range(yIzq,yDer):
                    b,g,r = bgrImg[x,y]
                    b_prom += b
                    g_prom += g
                    r_prom += r
                    total += 1

            b_prom = b_prom // total
            g_prom = g_prom // total
            r_prom = r_prom // total

            for x in range(xIzq,xDer):
                for y in range(yIzq,yDer):
                    pixeles[x, y] = b_prom,g_prom,r_prom
                    # pixeles[x, y] = b,g,r ## creo que en esta se ve mejor

        return self.imagen
