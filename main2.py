import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg

path=r"C:\Users\Aditya.gupta\Desktop\Fun Projects\Draw_diff\rc.jpg.png"
imageList = [path, path, path]
coordinatesList = [[0, 0], [100, 200], [200, 200]]

ax = plt.gca()
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)
plt.hlines(150,10,400,linestyles='solid',colors='black',lw=1)
plt.hlines(130,20,400,linestyles='solid',colors='red',lw=1)

imgplot = [None] * len(imageList)
for i in range(1):
    imageFile = imageList[i]
    img=mpimg.imread(imageFile)
    tx, ty = 50,50
    ax.imshow(img, extent=(tx, tx + 20, ty, ty + 20))

plt.show()