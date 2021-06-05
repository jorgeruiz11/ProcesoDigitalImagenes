import cv2
import numpy as np
from PIL import Image
from os import remove
from os import path
import os
import sys
import random

np.seterr(over='ignore')

class ManejadorImagen(object):

    def __init__(self, ruta_imagen):
        self.imagen1 = cv2.imread(ruta_imagen)

        scale_percent = 20 # percent of original size
        width = int(self.imagen1.shape[1] * scale_percent / 100)
        height = int(self.imagen1.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        self.imagen = cv2.resize(self.imagen1, dim)
        self.ancho, self.alto, c = self.imagen.shape


    def cuadricula(self, size):
        x, y = size[0], size[1]
        l_coordenadas = []
        
        yIzq = 0
        yDer = y
        while yDer < self.alto:
            xIzq = 0
            xDer = x
            while xDer < self.ancho:
                l_coordenadas.append((xIzq, yIzq, xDer, yDer))

                xIzq = xDer
                xDer = xDer + x
            
            xDer = self.ancho - 1
            l_coordenadas.append((xIzq, yIzq, xDer, yDer))

            yIzq = yDer
            yDer = yDer + y
        
        yDer = self.alto - 1

        xIzq = 0
        xDer = x
        while xDer < self.ancho:
            l_coordenadas.append((xIzq, yIzq, xDer, yDer))

            xIzq = xDer
            xDer = xDer + x

        xDer = self.ancho - 1
        l_coordenadas.append((xIzq, yIzq, xDer, yDer))

        return l_coordenadas


    def mosaico_color(self, l_coordenadas, tam, titulo, font_size):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        # html_img = open('prueba.html', 'w')
        html_img = open(titulo, 'w')
        html_img.write('<FONT SIZE=font_size> <PRE>')

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

            color = '#%02x%02x%02x' % (r_prom, g_prom, b_prom) if (tam[0] > 7 or tam[1] > 7) else '#%02x%02x%02x' % (r, g, b)

            c_letras += f'<font color={color}>M'

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras + '<PRE>')
        html_img.close()


    def mosaico_gris(self, l_coordenadas, titulo, font_size):
        bgrImg = self.imagen

        html_img = open(titulo, 'w')
        html_img.write('<FONT SIZE=font_size> <PRE>')

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

        html_img.write(c_letras + '<PRE>')
        html_img.close()


    def mosaico_simbolosBW(self, l_coordenadas, titulo, font_size):
        bgrImg = self.imagen

        html_img = open(titulo, 'w')
        html_img.write('<FONT SIZE=font_size> <PRE>')

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


    def mosaico_simbolosC(self, l_coordenadas, tam, titulo, font_size):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        html_img = open(titulo, 'w')
        html_img.write('<FONT SIZE=font_size> <PRE>')

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

            color = '#%02x%02x%02x' % (r_prom, g_prom, b_prom) if (tam[0] > 7 or tam[1] > 7) else '#%02x%02x%02x' % (r, g, b)

            gris = (b + g + r) // 3
            simbolo = self.define_simbolo(gris)
            c_letras += f'<font color={color}>{simbolo}'

            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras + '<PRE>')
        html_img.close()


    def mosaico_simbolos_BW_tonos(self, l_coordenadas, titulo, font_size):
        bgrImg = self.imagen

        html_img = open(titulo, 'w')
        html_img.write('<FONT SIZE=font_size> <PRE>')

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

        html_img.write(c_letras + '<PRE>')
        html_img.close()


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



    def mosaico_texto(self, l_coordenadas, tam, titulo, font_size, texto):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        html_img = open(titulo, 'w')
        html_img.write('<FONT SIZE=font_size> <PRE>')

        c_letras = ''
        i = 0

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

            color = '#%02x%02x%02x' % (r_prom, g_prom, b_prom) if (tam[0] > 7 or tam[1] > 7) else '#%02x%02x%02x' % (r, g, b)

            if i < len(texto):
                c_letras += f'<font color={color}>{texto[i]}'
                i += 1
            else:
                i = 0
                c_letras += f'<font color={color}>{texto[i]}'


            if xIzq == 0:
                c_letras += '<br>'

        html_img.write(c_letras + '<PRE>')
        html_img.close()


    def domino_blanco(self, l_coordenadas, titulo):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        txt_img = open(titulo, 'w')

        c_letras = ''
        ficha = ''
        primer_lado_ficha = False # False => 0

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

            gris = (b_prom + g_prom + r_prom) // 3

            if gris in range(0,26):
                ficha = '9('[primer_lado_ficha] # Si es False => '9('[0], True => '9('[1]
            elif gris in range(26,52):
                ficha = '8i'[primer_lado_ficha]
            elif gris in range(52,78):
                ficha = '7&'[primer_lado_ficha]
            elif gris in range(78,104):
                ficha = '6^'[primer_lado_ficha]
            elif gris in range(104,130):
                ficha = '5%'[primer_lado_ficha]
            elif gris in range(130,156):
                ficha = '4$'[primer_lado_ficha]
            elif gris in range(156,182):
                ficha = '3#'[primer_lado_ficha]
            elif gris in range(182,208):
                ficha = '2@'[primer_lado_ficha]
            elif gris in range(208,234):
                ficha = '1!'[primer_lado_ficha]
            elif gris in range(234,255):
                ficha = '0)'[primer_lado_ficha]

            primer_lado_ficha = not primer_lado_ficha
            c_letras += ficha

            if xIzq == 0:
                c_letras += '\n'

        txt_img.write(c_letras)
        txt_img.close()


    def domino_negro(self, l_coordenadas, titulo):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        txt_img = open(titulo, 'w')

        c_letras = ''
        ficha = ''
        primer_lado_ficha = False

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

            gris = (b_prom + g_prom + r_prom) // 3

            if gris in range(0,26):
                ficha = '0)'[primer_lado_ficha]
            elif gris in range(26,52):
                ficha = '1!'[primer_lado_ficha]
            elif gris in range(52,78):
                ficha = '2@'[primer_lado_ficha]
            elif gris in range(78,104):
                ficha = '3#'[primer_lado_ficha]
            elif gris in range(104,130):
                ficha = '4$'[primer_lado_ficha]
            elif gris in range(130,156):
                ficha = '5%'[primer_lado_ficha]
            elif gris in range(156,182):
                ficha = '6^'[primer_lado_ficha]
            elif gris in range(182,208):
                ficha = '7&'[primer_lado_ficha]
            elif gris in range(208,234):
                ficha = '8i'[primer_lado_ficha]
            elif gris in range(234,255):
                ficha = '9('[primer_lado_ficha]

            primer_lado_ficha = not primer_lado_ficha
            c_letras += ficha


            if xIzq == 0:
                c_letras += '\n'

        txt_img.write(c_letras)
        txt_img.close()


    def cartas(self, l_coordenadas, titulo):
        rgbImg = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        txt_img = open(titulo, 'w')

        c_letras = ''
        carta = ''

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

            gris = (b_prom + g_prom + r_prom) // 3

            if gris in range(0,24):
                carta = random.choice('klm')
            elif gris in range(24,48):
                carta = 'j'
            elif gris in range(48,72):
                carta = 'i'
            elif gris in range(72,96):
                carta = 'h'
            elif gris in range(96,120):
                carta = 'g'
            elif gris in range(120,144):
                carta = 'f'
            elif gris in range(144,168):
                carta = 'e'
            elif gris in range(168,192):
                carta = 'd'
            elif gris in range(192,216):
                carta = 'c'
            elif gris in range(216,240):
                carta = 'b'
            elif gris in range(240,255):
                carta = 'a'

            c_letras += carta

            if xIzq == 0:
                c_letras += '\n'

        txt_img.write(c_letras)
        txt_img.close()



if __name__ == '__main__':
    m = ManejadorImagen('back.jpeg')
    titulo = "pr1.html"
    tam = [1,1]
    imgP = m.cuadricula(tam)
    # img = m.mosaico_color(imgP, tam, titulo)
    # img = m.mosaico_gris(imgP, titulo)
    # img = m.mosaico_simbolosBW(imgP, titulo)
    # img = m.mosaico_simbolosC(imgP, tam, titulo)
    # img = m.mosaico_simbolos_BW_tonos(imgP, titulo)
    # img = m.mosaico_texto(imgP, tam, titulo, "HOLA ")
    img = m.cartas(imgP, titulo)
    # img = m.domino_blanco(imgP, titulo)
    # img = m.domino_negro(imgP, titulo)