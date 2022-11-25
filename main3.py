
from matplotlib import pyplot as plt 
import pandas as pd
import matplotlib.image as mpimg

global y_divider1,y_divider2,y_road1,y_road2,y_roadside1,y_roadside2,x,len,y
y,x,len=0,2,1

def get_df():
    return pd.read_excel(r'Untitled 1.xls')

def get_divider(d=3):
    global y_divider1,y_divider2,y
    y_divider1=y+d/2
    y_divider2=y-d/2
    plt.hlines(y_divider1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_divider2,x,x+len,linestyles='solid',colors='black',lw=1)

def get_road(d1=9,d2=9,d3=8.5):
    global y_road1,y_road2
    try:
        y_road1=y_divider1+d1
        y_road2=y_divider2-d2
    except:
        y_road1=d1
        y_road2=-d2
    plt.hlines(y_road1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_road2,x,x+len,linestyles='solid',colors='black',lw=1)

    ##Drawing mid-road lines
    plt.hlines(y_divider1+d1/2,x,x+len,linestyles='dashed',colors='blue',lw=1)
    plt.hlines(y_divider2-d2/2,x,x+len,linestyles='dashed',colors='blue',lw=1)

    ##Get ofc line
    plt.hlines(y_divider2-d2/2-d3,x,x+len,linestyles='dashed',colors='red',lw=2)



def get_roadside(d1=5,d2=5):
    global y_roadside1,y_roadside2
    y_roadside1=y_road1+d1
    y_roadside2=y_road2-d2
    plt.hlines( y_roadside1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_roadside2,x,x+len,linestyles='solid',colors='black',lw=1)    

def outer_box(d=3):
    
    yl=y_roadside1+d
    yr=y_roadside2-d-2
    plt.hlines(yl,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(yr,x,x+len,linestyles='solid',colors='black',lw=1)       

def get_objects_roadside(d=1):
    yl=y_roadside1+d
    yr=y_roadside2-d-d/2    
    df=get_df()
    #print(df.index)
    #print(df,len(df.index))
    for i in df.index:
        print(float(df['Chainage'][i]),d,df['RHS'][i])
        plt.text(float(df['Chainage'][i]),yr,df['RHS'][i],fontsize = 9,color='Black')
        plt.text(float(df['Chainage'][i]),yl,df['LHS'][i],fontsize = 9,color='Black')


def get_chainage(d=3):
    df=get_df()
    yr=y_roadside2-d

    for i in df.index:
        plt.text(float(df['Chainage'][i]),yr,df['Chainage'][i],fontsize = 10,color='Black',rotation=90)


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


fig=plt.figure(figsize=(30,8))   
ax = plt.gca()
ax.set_xlim(x-0.09, x+len+0.09)
plt.axis('off')
# get_divider()
# get_road()
#get_roadside()
# outer_box(7)
get_objects_roadside()
# get_chainage()

#plt.hlines(3,0,1,linestyles='solid',colors='black',lw=1)
plt.show()















