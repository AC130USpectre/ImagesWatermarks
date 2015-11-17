import os
import os.path

def noise(usernumber, userquantity, coordinate, dimension, seed):#вычисление координаты шума для нужной координаты нужного юзера
    noiseFileName = str(userquantity) + '-' + str(dimension) + '-' + str(seed) + '.txt'#файл с векторами шума
    if not (os.path.exists(noiseFileName) and os.path.isfile(noiseFileName)):#если файла раньше не было, создаём его, используя заранее скомпилированный noiseGen.cpp
        print('Создаю новый файл шума!')
        noiseCommand = 'noiseGen ' + str(seed) + ' ' + str(userquantity) + ' ' + str(dimension) + ' ' + noiseFileName
        os.system(noiseCommand)
    file = open(noiseFileName, 'r')#файл с шумом точно есть
    return float(file.readlines()[coordinate].split(' ')[usernumber])
