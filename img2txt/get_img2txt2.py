# -*- coding: UTF-8 -*-
from PIL import Image
import os

serarr = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
count = len(serarr)


def toText(image_file):  # 此函数不能输入 gif 文件
    image_file = image_file.convert("L")  # 转灰度
    asd = ''  # 储存字符串
    for h in range(0, image_file.size[1]):  # h
        for w in range(0, image_file.size[0]):  # w
            gray = image_file.getpixel((w, h))
            asd = asd + serarr[int(gray / (256 / (count)))]
        asd = asd + '\r\n'
    return asd


def toText2(image_file):
    asd = ''  # 储存字符串
    for h in range(0, image_file.size[1]):  # h
        for w in range(0, image_file.size[0]):  # w
            r, g, b = image_file.getpixel((w, h))
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            asd = asd + serarr[int(gray / (256 / (count)))]
        asd = asd + '\r\n'
    return asd


image_file = Image.open("dingdang.png")  # 打开图片
image_file = image_file.resize((int(image_file.size[0] * 0.5), int(image_file.size[1] * 0.5)))  # 调整图片大小
print (u'Info:', image_file.size[0], ' ', image_file.size[1], ' ', count)

tmp = open('tmp.txt', 'w')
tmp.write(toText(image_file))
tmp.close()