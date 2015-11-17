from PIL import Image, ImageDraw
import math, os
from Convert import direct

def imposeNoise(originalname, copyname, usernumber, userquantity, cluster_w, cluster_h):
#берём оригинал, накладываем на него шум и запиываем в копию
    original = Image.open(originalname).convert("RGB")#убираем альфа-канал, если он был
    (width, height) = original.size#размеры картинки в пикселях
    pix = original.load()#массив пикселей картинки
#сколько целых кластеров помещается в картинке
    c_width = width // cluster_w
    c_height = height // cluster_h
#куда запишем копию
    watermark = Image.new("RGB", original.size, "white")
    draw = ImageDraw.Draw(watermark)
#аппаратно-зависимый максимальный сид
    max_seed = os.system('getMaxSignedInt') * 2 - 1
    seed = 0
    for i in range(width):#считаем seed по картинке
        for j in range(height):
            (a, b, c) = pix[i, j]
            seed += math.ceil((math.sin(a + b + c)**2)*(a + b + c))
    seed = seed % max_seed
    print('seed = ' + str(seed))

    for i_c in range(c_width + 1):#проходим по прямоугольным кластерам
        for j_c in range(c_height + 1):
            if (i_c == c_width):
                if (j_c == c_height):
                    for i in range(cluster_w * c_width, width):#бордюр изображения, не умещающийся в кластеры
                        for j in range(cluster_h * c_height, height):
                            draw.point((i, j), pix[i, j])
                else:
                    for i in range(cluster_w * c_width, width):
                        for j in range(cluster_h * j_c, cluster_h * (j_c + 1)):
                            draw.point((i, j), pix[i, j])
            else:
                if (j_c == c_height):
                    for i in range(cluster_w * i_c, cluster_w * (i_c + 1)):
                        for j in range(cluster_h * c_height, height):
                            draw.point((i, j), pix[i, j])
                else:
                    rect = (cluster_w * i_c, cluster_h * j_c, cluster_w * (i_c + 1), cluster_h * (j_c + 1))#выделенный прямоугольный кластер
                    watermark.paste(direct(original.crop(rect), usernumber, userquantity, j_c * c_width + i_c, c_width * c_height, seed), rect)#вставляем в копию новый кластер

    watermark.save(copyname)
    del draw
