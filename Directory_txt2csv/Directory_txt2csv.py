# -*- encoding: utf-8 -*-
"""
@File    : Directory_txt2csv.py
@Time    : 2019/10/3 13:44
@Author  : cxloge
@Email   : cxloge@126.com
@Software: PyCharm
"""

import re

with open('Directory.txt','r',encoding='UTF-8') as f:
    # id_lines = []
    # id_line_tags = []
    # page_lines = []
    # name_lines = []
    for line in f.readlines():
        line = line.strip()
        if len(line) != 0:
            if len(line.split()) >= 2:
                # id_line = line.split()[0].replace('．','.') # 替换符号
                id_line = line.split()[0]
                # 添加id_line_tag 分级标题
                if len(id_line.split('.')) == 2:
                    # id_line_tag = (r'\t%s'%id_line)
                    id_line_tag = (r'\t%s'%id_line)
                    # print(id_line_tag)176 8808 2577
                elif len(id_line.split('.')) == 3:
                    # id_line_tag = (r'\t\t%s'%id_line)
                    id_line_tag = (r'\t\t%s'%id_line)
                else:
                    id_line_tag = id_line
                    # print(id_line_tag)
                # page_line = line.split()[-1]
                # name_line = re.sub(r'\W', '_','_'.join(line.split()[1:-1]))
                name_line = re.sub(r'\W', '_','_'.join(line.split()[1:]))
                # name_line ='_'.join(line.split()[1:-1])
            # 组装数组保存数据
            # id_lines.append(id_line)
            # id_line_tags.append(id_line_tag)
            # page_lines.append(page_line)
            # name_lines.append(name_line)
    # print(id_line_tags.append(id_lines))
            with open('Directory.csv','a',encoding='UTF-8') as f:
                # f.write(','.join(line.split()) + '\n')
                # f.write('%s|%s|%s|%s|%s \n'%(id_line_tag,id_line,name_line,page_line,line))
                f.write('%s|%s|%s|%s \n'%(id_line_tag,id_line,name_line,line))

"""

"""


