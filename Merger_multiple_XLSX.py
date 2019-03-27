# -*- coding: utf-8 -*-
"""
Created on Thrusday March  28 03:30:44 2019

@author: Sanu
"""

import os
import os.path
import numpy as np
import pandas as pd
import glob

path = "D:/BALIC_Outboud/"
file_identifier = "*.xlsx"

# display the files having extension .xlsx
for root,dirs,files in os.walk(path):
    files = [ _ for _ in files if _.endswith('.xlsx') ]
    for xlsfile in files:
        print ("File in mentioned folder is: " + xlsfile)

all_data = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True, sort=False)


# now save the data frame
writer = pd.ExcelWriter('output.xlsx')
all_data.to_excel(writer,'sheet1')
writer.save()
