import numpy as np
import cv2
import os
from os import remove
from os import path
from PIL import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tqdm import tqdm

np.seterr(over='ignore')

def muestra_resultado(imagen):
    imagen.show()

def guarda_resultado(titulo, imagen):
    imagen.save(titulo)
    return titulo

def borra_resultado(titulo):
    if path.exists(titulo):
        remove(titulo)

class ManejadorImagen(object):

    def __init__(self, ruta_imagen):
        c_img = cv2.imread(ruta_imagen)
        img = Image.open(ruta_imagen)

        self.imagen = cv2.resize(c_img, (500,400))
        self.Pimagen = img.resize((500,400), Image.ANTIALIAS)

        self.ancho, self.alto = self.Pimagen.size

        self.nombreImg = self.getNombre(ruta_imagen)

    def calcula_regiones(self, tam, size):
        x, y = size[0], size[1]
        l_coords = []
        yIzq = 0
        yDer = y

        while yDer < tam[1]:
            xIzq = 0
            xDer = x
            while xDer < tam[0]:
                l_coords.append((xIzq,yIzq,xDer,yDer))

                xIzq = xDer
                xDer += x

            xDer = tam[0] - 1
            l_coords.append((xIzq,yIzq,xDer,yDer))

            yIzq = yDer
            yDer += y

        yDer = tam[1] - 1

        xIzq = 0
        xDer = x
        while xDer < tam[0]:
            l_coords.append((xIzq,yIzq,xDer,yDer))
            xIzq = xDer
            xDer += x

        xDer = tam[0] - 1
        l_coords.append((xIzq,yIzq,xDer,yDer))

        return l_coords


    def gen_gray_images(self, size):
        rgbImg = Image.fromarray(self.imagen)
        modImg = self.Pimagen.load()

        brillo = -255
        cte = 17

        gris_tonos = []

        if not os.path.exists(f'{self.nombreImg}_imagesBW'):
            os.mkdir(f'{self.nombreImg}_imagesBW')

        # Crearemos solamente 30 imagenes, es decir, 30 tonos.
        j = 1
        porcentaje = tqdm(total=30, position=0, leave=False)

        for i in range(30):
            imgToPixel = self.Pimagen.load()
            grisProm = 0
            c = 1

            for x in range(self.ancho):
                for y in range(self.alto):
                    r,g,b = rgbImg.getpixel((x,y))
                    gris = (r+g+b) / 3

                    nR = (gris + brillo)
                    nG = (gris + brillo)
                    nB = (gris + brillo)

                    r = 0 if nR < 0 else (255 if nR > 255 else int(nR))
                    g = 0 if nG < 0 else (255 if nG > 255 else int(nG))
                    b = 0 if nB < 0 else (255 if nB > 255 else int(nB))
                    imgToPixel[x,y] = (r,g,b)

                    grisProm += (r+g+b) / 3
                    c += 1

            gris_tonos.append(grisProm / c)

            # porcentaje = int(j * 100 / 30)
            # print(f'{j}/{30} | {porcentaje}%', end='\r')
            porcentaje.set_description('Procesando...'.format(j))
            j += 1
            porcentaje.update(1)

            if not os.path.exists(f'{self.nombreImg}_imagesBW/{self.nombreImg}_{i}_.jpg'):
                self.Pimagen.save(f'{self.nombreImg}_imagesBW/{self.nombreImg}_{i}.jpg')

            brillo += cte

        porcentaje.close()
        imgToPixel = self.Pimagen.load()

        for x in range(self.ancho):
            for y in range(self.alto):
                r,g,b = rgbImg.getpixel((x,y))
                gris = int((r+g+b) / 3)
                imgToPixel[x,y] = (gris, gris, gris)

        l_coords = self.calcula_regiones(self.Pimagen.size, (size[0],size[1]))
        imgInCoord = []

        total = len(l_coords)

        for (xIzq, yIzq, xDer, yDer) in l_coords:
            g_prom = 0
            c = 1

            for x in range(xIzq, xDer):
                for y in range(yIzq, yDer):
                    gris, _, _ = self.Pimagen.getpixel((x,y))
                    g_prom += gris
                    c += 1

            g_prom /= c
            tonoCernano = gris_tonos.index(min(gris_tonos, key=lambda im:abs(im-g_prom)))
            imgInCoord.append(tonoCernano)

            if xDer >= self.ancho -1:
                imgInCoord.append(-1)


        posX = 0
        posY = 0
        nuevoAncho = (int) (self.ancho / size[0]) * size[0]
        nuevoAlto = (int) (self.alto / size[1]) * size[1]

        ImgMadeOfImgs = Image.new('RGB', (nuevoAncho, nuevoAlto), (255, 255, 255, 255))
        pixeles = [Image.open(f'{self.nombreImg}_imagesBW/{self.nombreImg}_{i}.jpg') for i in range(30)]
        pixeles = [img.resize(size) for img in pixeles]

        for indice in imgInCoord:
            if indice == -1:
                posX = 0
                posY += size[1]
            else:
                img = pixeles[indice]
                ImgMadeOfImgs.paste(img, (posX, posY))
                posX += size[0]

        ImgMadeOfImgs.save(f'{self.nombreImg}_Result_BW.jpg')

        return ImgMadeOfImgs


    def gen_color_images(self, size):
        rgbImg = Image.fromarray(self.imagen)
        modImg = self.Pimagen.load()

        l_coords = self.calcula_regiones(self.Pimagen.size, (size[0],size[1]))
        total = len(l_coords)

        posX = 0
        posY = 0
        nuevoAncho = (int) (self.ancho / size[0]) * size[0]
        nuevoAlto = (int) (self.alto / size[1]) * size[1]

        ImgMadeOfImgs = Image.new('RGB', (nuevoAncho, nuevoAlto), (255, 255, 255, 255))
        imgToPixel = self.Pimagen.load()

        img_i = 1
        porcentaje = tqdm(total=30, position=0, leave=False)

        for (xIzq, yIzq, xDer, yDer) in l_coords:
            rProm = 0
            gProm = 0
            bProm = 0
            c = 1

            for x in range(xIzq, xDer):
                for y in range(yIzq, yDer):
                    r, g, b = rgbImg.getpixel((x,y))
                    rProm += r
                    gProm += g
                    bProm += b
                    c += 1

            rProm = int(rProm / c)
            gProm = int(gProm / c)
            bProm = int(bProm / c)

            for x in range(self.ancho):
                for y in range(self.alto):
                    r, g, b = rgbImg.getpixel((x,y))
                    imgToPixel[x,y] = (bProm & b, gProm & g, rProm & r)

            pixelResize = self.Pimagen.resize(size)
            ImgMadeOfImgs.paste(pixelResize, (posX, posY))



            # porcentaje = int(img_i * 100 / total)
            # print(f'{img_i}/{total} | {porcentaje}%', end='\r')
            porcentaje.set_description('Procesando...'.format(j))
            img_i += 1
            porcentaje.update(1)

            posX += size[0]
            if xDer >= self.ancho - 1:
                posX = 0
                posY += size[1]

            ImgMadeOfImgs.save(f'{self.nombreImg}_Result_Color.jpg')

        return ImgMadeOfImgs


    # con este nombre crearemos el directorio y los titulos de las
    # imagenes en BW
    def getNombre(self, ruta_imagen):
        nameOut = ""
        if('.jpeg' in ruta_imagen):
            nameOut = ruta_imagen.replace('.jpeg', "")
        if('.jpg' in ruta_imagen):
            nameOut = ruta_imagen.replace('.jpg', "")
        if('.png' in ruta_imagen):
            nameOut = ruta_imagen.replace('.png', "")

        return nameOut



# if __name__ == '__main__':
#     m = ManejadorImagen('back.jpeg')
#     # m.gen_gray_images((10,10))
#     m.gen_color_images((20,20))
