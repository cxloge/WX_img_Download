# -*- coding: utf-8 -*-

# from urllib.parse import urlsplit,urlparse
import re
import time
import os
from urllib.parse import urlparse

from PIL import Image
import requests
import numpy as np
import pandas as pd

# 替换markdown img 文本
# 在img添加文件关键字

# wx_img = r'https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDFcQVoczkWr1Y1CyWT9hVMbiaAaw2gCPpoT1oK1so42cenyRwfPjk7xw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1'

# urlsplit()
# from urllib.parse import urlsplit
# 与urlparse类似，但urlsplict把urlstirng分割成5个部分，其中少了paramters

# wx_img_new = urlsplit(wx_img)
# wx_img_new = urlparse(wx_img)

# ParseResult(scheme='https',
# netloc='mmbiz.qpic.cn',
# path='/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDFcQVoczkWr1Y1CyWT9hVMbiaAaw2gCPpoT1oK1so42cenyRwfPjk7xw/640',
# params='',
# query='wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1',
# fragment='')

# 取出文件类型

def get_wx_img_type(wx_img):
    wx_img_type = urlparse(wx_img)[4].split("&")[0].split("=")[1]
    return wx_img_type

# 通过markdown获取下载链接
# md_name = r'向 Excel 说再见，神级编辑器统一表格与 Python.md'

def get_url_md(md_name):
    img_names = [ ]
    img_urls = [ ]
    img_types = [ ]
    with open(md_name) as f:
        count = 1
        for line in f:
            count = count +1
            # print(count)
            get_md_img_url = re.match(r'(^!.*)',line)
            if get_md_img_url != None:
                # 获取当前时间戳  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                # time.strftime('%Y-%m-%d', time.localtime(time.time()))
                time_strftime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                img_name = line.split("[")[1].split("]")[0]+ '_' + time_strftime +'_' + str(count)
                img_names.append(img_name)
                # print(img_names)
                img_url = line.split("(")[1].split(')')[0]
                img_urls.append(img_url)
                img_type = urlparse(img_url)[4].split("&")[0].split("=")[1]
                img_types.append(img_type)
                # print(line)
                # print(img_url)
            # url = re.match(r'(^!.*)',line)
            # print(url)
        img_all = np.array([img_names,img_urls,img_types])
        data_df = pd.DataFrame(img_all)
        # create and writer pd.DataFrame to excel
        # 数组装置transpose()
        data_df = data_df.transpose()
        writer = pd.ExcelWriter('Save_Excel.xlsx')
        data_df.to_excel(writer, 'page_1')  #
        writer.save()
        print("img_all",img_all)
    return img_names,img_urls,img_types



# webp转换为jgp
# im = Image.open(path)
# im.save(path, 'JPEG')

# 替换markdown img 文本
def re_markdown_img(md_name):
    with open(md_name) as f1:
        for line in f1.readlines():
            line = line.strip()
            print(line)
            if len(line) != 0:
                # 获取img替换为本地链接
                get_md_img_url = re.match(r'(^!.*)', line)
                if get_md_img_url != None:
                    for local_img_md in line_new_img():
                        line = line.replace(line,local_img_md) # 数据获取不统一
                        print("img_url"+line)
                with open('new.md','a',encoding='UTF-8') as f2:
                    f2.write(line + '\n' )

def line_new_img():
    keyword = 'Python_Excel_gridstudio_'
    # 组装路径与下载链接
    root = "./images/"

    img_arrys = get_url_md(md_name)
    # print(img_arrys)
    # print(range(len(img_arrys)))
    # for img_arry in img_arrys:
    local_img_mds = []
    for i in range(len(img_arrys)):
        for j in  range(len(img_arrys[i])):
            # print(img_arrys[i][j])
            img_name = keyword + img_arrys[0][j]
            img_url = img_arrys[1][j]
            img_type = img_arrys[2][j]
            local_img = root + img_name + '.' + img_type
            # 拼接本地img字符
            local_img_md = '![' + img_name + '](' + local_img + ')'
            local_img_mds.append(local_img_md)
            print(local_img)
            # print(img_name,img_url,img_type)
    return local_img_mds

def download_img(img_name,img_url,img_type):
    # 组装路径与下载链接
    root = "./images/"
    path = root + img_name + '.' +img_type
    print(path)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(img_url)
            r.raise_for_status()
        # 使用with语句可以不用自己手动关闭已经打开的文件流
            with open(path, "wb") as f:  # 开始写文件，wb代表写二进制文件
                f.write(r.content)
            if img_type == 'png':
                im = Image.open(path)
                im.save(path,img_type)
            print("爬取完成")
        else:
            print("文件已存在")
    except Exception as e:
            print("爬取失败:" + str(e))



if __name__ == '__main__':
    # wx_img_type = get_wx_img_type(wx_img)
    # print (wx_img_type)
    keyword = 'Python_Excel_gridstudio_'

    md_name = r'向 Excel 说再见，神级编辑器统一表格与 Python.md'
    img_arrys = get_url_md(md_name)
    print(img_arrys)
    # # print(range(len(img_arrys)))
    # # for img_arry in img_arrys:
    # for i in range(len(img_arrys)):
    #     for j in  range(len(img_arrys[i])):
    #         # print(img_arrys[i][j])
    #         img_name = keyword + img_arrys[0][j]
    #         img_url = img_arrys[1][j]
    #         img_type = img_arrys[2][j]
    #         print(img_name,img_url,img_type)
    #         download_img(img_name,img_url,img_type)
    re_markdown_img(md_name)
    # line_new_img()
    # re_markdown_img()
