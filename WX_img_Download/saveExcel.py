# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:57:34 2017

@author: Bruce Lau
"""

import numpy as np
import pandas as pd
# from openpyxl.workbook import Workbook

# # prepare for data
# data = np.arange(1,101).reshape((10,10))
# data_df = pd.DataFrame(data)
#
# # change the index and column name
# data_df.columns = ['A','B','C','D','E','F','G','H','I','J']
# data_df.index = ['a','b','c','d','e','f','g','h','i','j']
#
# # create and writer pd.DataFrame to excel
# writer = pd.ExcelWriter('Save_Excel.xlsx')
# data_df.to_excel(writer,'page_1',float_format='%.5f') # float_format 控制精度
# writer.save()


# import numpy as np
# world=np.zero([5,5])
# for i in range(0,world.shape[0])
#     for j in range(0,world.shape[1])
#         print (world[i][j])

sheet = pd.read_excel('Save_Excel.xlsx')


# 取出img
for i in range(0,sheet.shape[0]):
    print(sheet[0][i])
    print(sheet[1][i])
    print(sheet[2][i])