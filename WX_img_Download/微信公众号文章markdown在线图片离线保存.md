# 微信公众号文章markdown在线图片离线保存

## 读取md文件

```python
import os
os.chdir(r'C:\Users\ChenXiaolong\Documents\#Python#JupyterNotebooks')
md = r'小姐姐太强了，动图展示 10 大 Git 命令，不会都难.md'
with open(md,'r',encoding='utf8') as f:
    data = f.readlines()
```

## 获取md的图片链接

```python
## 从data读取出图片链接  http://mmbiz.qpic.cn

for text in data:
    text = text.strip('\n')
    if 'https://mmbiz.qpic.cn' in text:
#         print(type(text))
        print(text)
    # 保存图片URL到img_url ---todo
```

## 解析图片URL

```python
from urllib.parse import urlparse

url = r'https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gWicpG4ibricDjhseFOGY3Qnc47QerrsJKNIjX2kiaUcH5vgEhxWiavM0YewFoJF5EicMrkf03sibglPia8esQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1'

# 获取文件名
wx_url_path = urlparse(url).path.split('/')[-2]
# 图片类型
wx_fmt=urlparse(url).query.split('&')[0].split('=')[1]
img_name = wx_url_path + '.' + wx_fmt
print(img_name) 
## KmXPKA19gWicpG4ibricDjhseFOGY3Qnc47QerrsJKNIjX2kiaUcH5vgEhxWiavM0YewFoJF5EicMrkf03sibglPia8esQ.png

```

## 通过URL下载文件,文件名为img_name

```python
# from PIL import Image
import requests

# 当前路径
root = "./images/"
path = root + img_name
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
#         im = Image.open(path)
#         im.save(path, 'JPEG')
        print("爬取完成")
    else:
        print("文件已存在")
except Exception as e:
    print("爬取失败:"+str(e))
```

