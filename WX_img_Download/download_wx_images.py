# -*- coding: utf-8 -*-

import requests
import os
import csv
from PIL import Image
import re

# 当前路径
root = "./images/"

lines = [ ]
with open("wx_images.csv") as file:
    for line in file:
        lines.append(line)
        print(line)

# 通过markdown获取下载链接
md_name = r'向 Excel 说再见，神级编辑器统一表格与 Python.md'


def get_url_md(md_name):
    with open(md_name) as f:
        for line in  f:
            # 通过正则寻找img链接
            line = re.match(r'(^!.*)',line)
    return url


for i in range(len(lines)):
    # 拆分数组
    temp = lines[i].split(",")
    # 组装路径与下载链接
    path = root + temp[0] +".jpeg"
    url = temp[1]
    print(url)
    print(path)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            #使用with语句可以不用自己手动关闭已经打开的文件流
            with open(path,"wb") as f: #开始写文件，wb代表写二进制文件
                f.write(r.content)
            # webp转换为jgp
            im = Image.open(path)
            im.save(path, 'JPEG')
            print("爬取完成")
        else:
            print("文件已存在")
    except Exception as e:
        print("爬取失败:"+str(e))

# if __name__ == '__main__':

# # webp转换为jgp
# im = Image.open(path)
# im.save(path, 'JPEG')
# Python识别图像格式并转码(支持webp格式) https://www.jianshu.com/p/c9f0097be881