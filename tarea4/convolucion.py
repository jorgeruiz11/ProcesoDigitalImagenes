from PIL import Image
import numpy as np

class convolucion(object):

    def __init__(self, ruta_imagen):
        self.ruta = Image.open(ruta_imagen)
        wa, ha = self.ruta.size
        if wa > 800 or ha > 800:
            self.imagen = self.ruta.resize((600,500))
            self.ancho, self.alto = self.imagen.size
        else:
            self.imagen = self.ruta
            self.ancho, self.alto = self.imagen.size

    def blur(self):
        matriz = [
            [0.0,0.2,0.0],
            [0.2,0.2,0.2],
            [0.0,0.2,0.0]
        ]
        factor = 1.0
        bias = 0.0

        return self.conv(matriz, factor, bias)

    def blur2(self):
        matriz = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ]
        factor = 1.0/13.0
        bias = 0.0

        return self.conv(matriz, factor, bias)

    def motion_blur(self):
        matriz = [
            [1,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,1],
        ]
        factor = 1.0/9.0
        bias = 0.0

        return self.conv(matriz, factor, bias)

    def encontrar_bordes(self):
        matriz = [
            [0,0,-1,0,0],
            [0,0,-1,0,0],
            [0,0, 2,0,0],
            [0,0, 0,0,0],
            [0,0, 0,0,0]
        ]
        factor = 1.0
        bias = 0.0

        return self.conv(matriz, factor, bias)

    def sharpen(self):
        matriz = [
            [-1,-1,-1],
            [-1, 9,-1],
            [-1,-1,-1]
        ]
        factor = 1.0
        bias = 0.0

        return self.conv(matriz, factor, bias)

    def emboss(self):
        matriz = [
            [-1,-1,-1,-1,0],
            [-1,-1,-1,0, 1],
            [-1,-1,0, 1, 1],
            [-1,0, 1, 1,-1],
            [0, 1, 1, 1, 1]
        ]
        factor = 1.0
        bias = 128.0

        return self.conv(matriz, factor, bias)

    # hacer una copia de la original, trabajar normal con la escala de grises
    # y combinarlas
    def conv(self, matriz, factor, bias):
        w,h = self.ancho, self.alto
        grayImg = self.imagen.convert('L')
        rgbImg = grayImg.convert('RGB')
        # rgbImg = self.imagen.convert('RGB')

        matriznp = np.array(matriz)
        filtroW, filtroH = matriznp.shape

        for x in range(w):
            for y in range(h):
                bValor,gValor,rValor = 0.0,0.0,0.0

                for filtroX in range(filtroW):
                    for filtroY in range(filtroH):
                        imagenX = int(x - filtroW / 2 + filtroX + w) % w
                        imagenY = int(y - filtroH / 2 + filtroY + h) % h
                        r,g,b = rgbImg.getpixel((imagenX,imagenY))
                        valor = matriznp.item((filtroX,filtroY))
                        rValor += r * valor
                        gValor += g * valor
                        bValor += b * valor

                blue = min(max(int(factor * bValor + bias),0),255)
                green = min(max(int(factor * rValor + bias),0),255)
                red = min(max(int(factor * gValor + bias),0),255)
                self.imagen.putpixel((x,y),(red, green, blue))

        return self.imagen
