from GenerateNoise import noise
from PIL import Image, ImageDraw
import math

SCALE = 1#масштаб шума
def direct(rect, usernumber, userquantity, coordinate, dimension, seed):#наложить шум на прямоугольный кластер
    n = noise(usernumber, userquantity, coordinate, dimension, seed)
    n *= SCALE
    if (n == 0.0):
        return rect
    if (n > 0.0):
        n = math.floor(n)
    else:
        n = math.ceil(n)
    (width, height) = rect.size#размеры кластера
    pix = rect.load()#массив пикселей кластера
    draw = ImageDraw.Draw(rect)
    for i in range(width):#проход по всем пикселям кластера
        for j in range(height):
            (r, g, b) = pix[i, j]
            r += n; g += n; b += n
            if (r > 255):
                r = 255
            elif (r < 0):
                r = 0
            if (g > 255):
                g = 255
            elif (g < 0):
                g = 0
            if (b > 255):
                b = 255
            elif (b < 0):
                b = 0
            draw.point((i, j), (r, g, b))
    return rect

def diff(original, copy):#разница оригинала и копии
    pix_o = original.load()
    pix_c = copy.load()
    (width, height) = original.size
    diff = 0.0
    for i in range(width):
        for j in range(height):
            for k in range(2):#максимум модуля разности
                if (math.fabs(pix_c[i, j][k] - pix_o[i, j][k]) > diff):
                    diff = pix_c[i, j][k] - pix_o[i, j][k]
    return diff / SCALE
