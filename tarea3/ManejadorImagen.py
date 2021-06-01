import cv2
import numpy as np
from PIL import Image
from os import remove
from os import path
import os
import sys

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


    def cuadricula(self, size):
        x, y = size[0], size[1]
        l_coordenadas = []
        yIzq = 0
        yDer = y

        while yDer < self.alto:
            xIzq = 0
            xDer = x
            while xDer < self.ancho:
                l_coordenadas.append((xIzq,yIzq,xDer,yDer))
                xIzq = xDer
                xDer += x

            xDer = self.ancho - 1
            l_coordenadas.append((xIzq,yIzq,xDer,yDer))
            yIzq = yDer
            yDer += y

        yDer = self.alto - 1
        xIzq = 0
        xDer = x

        while xDer < self.ancho:
            l_coordenadas.append((xIzq,yIzq,xDer,yDer))
            xIzq = xDer
            xDer += x

        xDer = self.ancho - 1
        l_coordenadas.append((xIzq,yIzq,xDer,yDer))

        return l_coordenadas


    # Para el de color, probablemente no sea necesario calcular promedios. Es decir, no es necesario usar b_prom, etc
    # Cuando la cuadricula es pequeña ([1,1] hasta [10,10]) se ve mejor usando b,g,r.
    # Cuando la cuadricula es grande ([20,20] por ejemplo) se ve mejor usando b_prom,g_prom,r_prom.
    def mosaico_color(self, l_coordenadas, tam):
        # bgrImg = self.imagen
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        html_img = open('prueba.html', 'w')
        html_img.write('<FONT SIZE=1>')
        # html_img.write('<FONT SIZE=1> <PRE>')

        c_letras = ''

        for (xIzq,yIzq,xDer,yDer) in l_coordenadas:
            b_prom, g_prom, r_prom = 0,0,0
            total = 1

            for x in range(xIzq,xDer):
                for y in range(yIzq,yDer):
                    r,g,b = rgbImg[x,y]
                    r_prom += r
                    g_prom += g
                    b_prom += b
                    total += 1

            r_prom = r_prom // total
            g_prom = g_prom // total
            b_prom = b_prom // total

            if tam[0] < 7 and tam[1] < 7:
                color = '#%02x%02x%02x' % (b, g, r)
            else:
                color = '#%02x%02x%02x' % (r_prom, g_prom, b_prom)

            c_letras += f'<font color={color}>M'

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras)
        # html_img.write(c_letras + '</PRE>')
        html_img.close()

        return rgbImg


    def mosaico_gris(self, l_coordenadas):
        bgrImg = self.imagen

        html_img = open('prueba.html', 'w')
        html_img.write('<FONT SIZE=1>')

        c_letras = ''

        for (xIzq,yIzq,xDer,yDer) in l_coordenadas:
            b_prom, g_prom, r_prom = 0,0,0
            total = 1

            for x in range(xIzq, xDer):
                for y in range(yIzq, yDer):
                    b,g,r = bgrImg[x,y]
                    b_prom += b
                    g_prom += g
                    r_prom += r
                    total += 1

            b_prom = b_prom // total
            g_prom = g_prom // total
            r_prom = r_prom // total

            gris = (b_prom + g_prom + r_prom) // 3
            color = '#%02x%02x%02x' % (gris, gris, gris)
            c_letras += f'<font color={color}>M'

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras)
        html_img.close()

        return bgrImg


    def mosaico_simbolosBW(self, l_coordenadas):
        bgrImg = self.imagen

        html_img = open('prueba.html', 'w')
        html_img.write('<FONT SIZE=1> <PRE>')

        c_letras = ''

        for (xIzq,yIzq,xDer,yDer) in l_coordenadas:
            b_prom, g_prom, r_prom = 0,0,0
            total = 1

            for x in range(xIzq,xDer):
                for y in range(yIzq,yDer):
                    r,g,b = bgrImg[x,y]
                    b_prom += b
                    g_prom += g
                    r_prom += r
                    total += 1

            b_prom = b_prom // total
            g_prom = g_prom // total
            r_prom = r_prom // total

            gris = (b_prom + g_prom + r_prom) // 3

            simbolo = self.define_simbolo(gris)
            c_letras += simbolo

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras + '</PRE>')
        html_img.close()

        return bgrImg


    def mosaico_simbolosC(self, l_coordenadas, tam):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        html_img = open('prueba.html', 'w')
        html_img.write('<FONT SIZE=1>')

        c_letras = ''

        for (xIzq,yIzq,xDer,yDer) in l_coordenadas:
            b_prom, g_prom, r_prom = 0,0,0
            total = 1

            for x in range(xIzq,xDer):
                for y in range(yIzq,yDer):
                    r,g,b = rgbImg[x,y]
                    r_prom += r
                    g_prom += g
                    b_prom += b
                    total += 1

            r_prom = r_prom // total
            g_prom = g_prom // total
            b_prom = b_prom // total

            if tam[0] < 7 and tam[1] < 7:
                color = '#%02x%02x%02x' % (r, g, b)
            else:
                color = '#%02x%02x%02x' % (r_prom, g_prom, b_prom)

            gris = (b + g + r) // 3
            simbolo = self.define_simbolo(gris)
            c_letras += f'<font color={color}>{simbolo}'

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras)
        html_img.close()

        return rgbImg


    def mosaico_simbolos_BW_tonos(self, l_coordenadas):
        bgrImg = self.imagen

        html_img = open('prueba.html', 'w')
        html_img.write('<FONT SIZE=1>')

        c_letras = ''

        for (xIzq,yIzq,xDer,yDer) in l_coordenadas:
            b_prom, g_prom, r_prom = 0,0,0
            total = 1

            for x in range(xIzq,xDer):
                for y in range(yIzq,yDer):
                    r,g,b = bgrImg[x,y]
                    b_prom += b
                    g_prom += g
                    r_prom += r
                    total += 1

            b_prom = b_prom // total
            g_prom = g_prom // total
            r_prom = r_prom // total

            gris = (b_prom + g_prom + r_prom) // 3
            color = '#%02x%02x%02x' % (gris, gris, gris)

            simbolo = self.define_simbolo(gris)
            c_letras += f'<font color={color}>{simbolo}'

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras)
        html_img.close()

        return bgrImg


    def define_simbolo(self, num):
        letra = ''
        if num in range(0,16):
            letra = 'M'
        elif num in range(16,32):
            letra = 'N'
        elif num in range(32,48):
            letra = 'H'
        elif num in range(48,64):
            letra = '#'
        elif num in range(64,80):
            letra = 'Q'
        elif num in range(80,96):
            letra = 'U'
        elif num in range(96,112):
            letra = 'A'
        elif num in range(112,128):
            letra = 'D'
        elif num in range(128,144):
            letra = 'O'
        elif num in range(144,160):
            letra = 'Y'
        elif num in range(160,176):
            letra = '2'
        elif num in range(176,192):
            letra = '$'
        elif num in range(192,210):
            letra = '%'
        elif num in range(210,226):
            letra = '+'
        elif num in range(226,240):
            letra = '.'
        elif num in range(240,256):
            letra = ' '

        return letra


if __name__ == '__main__':
    m = ManejadorImagen('2.jpeg')
    tam = [1,1]
    imgP = m.cuadricula(tam)
    # img = m.mosaico_color(imgP, tam)
    # img = m.mosaico_gris(imgP)
    img = m.mosaico_simbolosBW(imgP)
    # img = m.mosaico_simbolosC(imgP, tam)
