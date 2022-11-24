import os
import numpy as np
import pandas as pd
import shutil

path1=r"C:\Users\Aditya.gupta\Downloads\Penpahad 15 Span - 1\Penpahad 15 Span"
path2=r"C:\Users\Aditya.gupta\Downloads\Penpahad 15 Span - 1"
file_src=os.listdir(path1)
file_dst=os.listdir(path2)

for i in (file_src):
    f=os.listdir((os.path.join(path1,i)))
    for j in f:
        if j[-4:]=='xlsx':
            print(j)
            shutil.copy(os.path.join(path1,i,j), path2)