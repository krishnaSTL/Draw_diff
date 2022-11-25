
from matplotlib import pyplot as plt 
import pandas as pd
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

global y_divider1,y_divider2,y_road1,y_road2,y_roadside1,y_roadside2,x,len,y
y,x,len=0,2000,1000

def get_df(x=2000):
    df=pd.read_excel(r'NHAI Data (1).xlsx')
    df= df.sort_values(by= "Chainage")
    df = df.loc[df["Chainage"]<=x+1000]
    df = df.loc[df["Chainage"]>=x]
    return df

def get_divider(d=300):
    global y_divider1,y_divider2,y
    y_divider1=y+d/2
    y_divider2=y-d/2
    plt.hlines(y_divider1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_divider2,x,x+len,linestyles='solid',colors='black',lw=1)

def get_road(d1=900,d2=900,d3=850):
    global y_road1,y_road2
    y_road1=y_divider1+d1
    y_road2=y_divider2-d2
    plt.hlines(y_road1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_road2,x,x+len,linestyles='solid',colors='black',lw=1)

    ##Drawing mid-road lines
    plt.hlines(y_divider1+d1/2,x,x+len,linestyles='dashed',colors='blue',lw=1)
    plt.hlines(y_divider2-d2/2,x,x+len,linestyles='dashed',colors='blue',lw=1)

    ##Get ofc line
    plt.hlines(y_divider2-d2/2-d3,x,x+len,linestyles='dashed',colors='red',lw=2)



def get_roadside(d1=500,d2=500):
    global y_roadside1,y_roadside2
    y_roadside1=y_road1+d1
    y_roadside2=y_road2-d2
    plt.hlines( y_roadside1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_roadside2,x,x+len,linestyles='solid',colors='black',lw=1)    

def outer_box(d=500):
    
    yl=y_roadside1+d+100
    yr=y_roadside2-d-300
    plt.hlines(yl,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(yr,x,x+len,linestyles='solid',colors='black',lw=1)       

def get_objects_roadside(d=100):
    yl=y_roadside1+d
    yr=y_roadside2-d-d/2    
    df=get_df()
    #print(df.index)
    #print(df,len(df.index))
    for i in df.index:
        #print(float(df['Chainage'][i]),d,df['RHS'][i])
        plt.text(float(df['Chainage'][i]),yr,df['Road side objects(RHS)'][i],fontsize = 9,color='Black')
        plt.text(float(df['Chainage'][i]),yl,df['Road side objects (LHS)'][i],fontsize = 9,color='Black')


def get_chainage(d=700):
    df=get_df()
    yr=y_roadside2-d

    for i in df.index:
        plt.text(float(df['Chainage'][i]),yr,df['Chainage'][i],fontsize = 10,color='Black',rotation=90)

def get_culvert():
    path=r"C:\Users\Aditya.gupta\Desktop\Fun Projects\Draw_diff\rc.jpg.png"
    path2=r'culvert_part.png'
    df=get_df()
    for i in df.index:
        if df['Culvert'][i]=="Yes":
            img=mpimg.imread(path)
            img2=mpimg.imread(path2)
            #print(np.shape(img))
            tx1, ty1 = df['Chainage'][i]+20,y_roadside1+250
            tx2, ty2 = df['Chainage'][i]+20,y_roadside2-250
            imagebox1 = OffsetImage(img, zoom = 0.15)
            imagebox2 = OffsetImage(img, zoom = 0.15)
            ab1 = AnnotationBbox(imagebox1, (tx1, ty1), frameon = False)
            ab2 = AnnotationBbox(imagebox2, (tx2, ty2), frameon = False)
            ax.add_artist(ab1)
            ax.add_artist(ab2)
            



def draw_sld():
    try:
        get_road(lwidth,rwidth)  #Drawing roads (left +Right)
        get_roadside(lwidth,rwidth) #Drawing roadside lines (left + Right)
        get_divider(d_half) #Drawing divider on road (at half of divider width)
        get_objects_roadside() #Drawing road side objects (if images)
        get_ofc_line(d)
        #get_culvert()
        #get_service_road(width,side,name)
        #get_fixed_things(coords)
        #Bridge(desc,coords,name)
        #get_soil()
       #get_chainage()

    except:
        print("All functions still not active")


fig=plt.figure(figsize=(3000,1000))   
ax = plt.gca()
ax.set_xlim(x-90, x+len+90)
#plt.axis('off')
get_divider()
get_road()
get_roadside()
outer_box()
get_objects_roadside()
get_chainage()
get_culvert()
#plt.hlines(3,0,1,linestyles='solid',colors='black',lw=1)
plt.show()















