from PIL import Image, ImageDraw
import math, os
from Convert import diff
from GenerateNoise import noise

#распознать копию

originalname = input("Путь к оригиналу: ")
copyname = input("Путь к копии: ")
cluster_w = int(input("Ширина кластера: "))
cluster_h = int(input("Высота кластера: "))
userquantity = int(input("Число пользователей: "))

original = Image.open(originalname).convert("RGB")
copy = Image.open(copyname)

if (copy.size != original.size):
    print("Размеры не совпадают!")
    sys.exit()

(width, height) = original.size
c_width = width // cluster_w
c_height = height // cluster_h

pix = original.load()

max_seed = os.system('getMaxSignedInt') * 2 - 1#тот же seed, который использовался при наложении шума
seed = 0
for i in range(width):
    for j in range(height):
        (a, b, c) = pix[i, j]
        seed += math.ceil((math.sin(a + b + c)**2)*(a + b + c))
seed = seed % max_seed

noise_list = []#получившийся в нелегальной копии вектор шума
for j_c in range(c_height):
    for i_c in range(c_width):
        rect = (cluster_w * i_c, cluster_h * j_c, cluster_w * (i_c + 1), cluster_h * (j_c + 1))
        noise_list.append(diff(original.crop(rect), copy.crop(rect)))

scalar_prod = []#скалярное произведение вектора шума с базисными векторами шума
for i in range(userquantity):
    summ = 0.0
    for j in range(c_width * c_height):
        summ += noise_list[j] * noise(i, userquantity, j, c_width * c_height, seed)
    scalar_prod.append(summ)

print(scalar_prod)#компоненты в ортогональном базисе 
input()
