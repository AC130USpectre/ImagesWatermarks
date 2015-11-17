from PIL import Image, ImageDraw

#побитовая сумма изображений с разными весами. Если сумма весов даёт 1, результат всегда корректен.

n = int(input("Число изображений: "))
weights = [0 for i in range(0, n)]
for i in range(0, n):
    weights[i] = float(input("Вес изображения №{}: ".format(str(i + 1))))
imagenames = [0 for i in range(0, n)]
for i in range(0, n):
    imagenames[i] = input("Путь к изображению №{}: ".format(str(i + 1)))

images = [0 for i in range(0, n)]
widths = [0 for i in range(0, n)]
heights = [0 for i in range(0, n)]
pixels = [0 for i in range(0, n)]
for i in range(0, n):
    images[i] = Image.open(imagenames[i])
    widths[i] = images[i].size[0]
    heights[i] = images[i].size[1]
    pixels[i] = images[i].load()

width = 0
height = 0
if (max(widths) == min(widths)):
    width = max(widths)
else:
    print("Картинки имеют разный размер!")
    sys.exit(0)
if (max(heights) == min(heights)):
    height = max(heights)
else:
    print("Картинки имеют разный размер!")
    sys.exit(0)

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)
rs = [0 for i in range(0, n)]
r = 0.0
gs = [0 for i in range(0, n)]
g = 0.0
bs = [0 for i in range(0, n)]
b = 0.0

for i in range(width):
    for j in range(height):
        for k in range(0, n):
            rs[k] = pixels[k][i, j][0]
            gs[k] = pixels[k][i, j][1]
            bs[k] = pixels[k][i, j][2]
        r = 0.0
        g = 0.0
        b = 0.0
        for k in range(0, n):
            r += rs[k] * weights[k]
            g += gs[k] * weights[k]
            b += bs[k] * weights[k]
        draw.point((i, j), (round(r), round(g), round(b)))

image.save("result.png", "PNG")
del draw
print("Выполнено!")
