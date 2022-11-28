
from matplotlib import pyplot as plt 
import pandas as pd
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

global y_divider1,y_divider2,y_road1,y_road2,y_roadside1,y_roadside2,x,len,y
y,x,len=0,2000,1000

def annonater(y1,y2,xl=2500,text=""):
        plt.annotate(
        '',xy=(xl, y1), xycoords='data',
        xytext=(xl, y2), textcoords='data',color='Red',
        arrowprops=dict(arrowstyle= '<->',color='red'))
        plt.annotate(
        abs(y1-y2), xy=(xl, (y1+y2)/2), xycoords='data',color='Red'
        )

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
    annonater(y_divider1,y_divider2,x+400)



def get_road(d1=900,d2=900,d3=850):
    global y_road1,y_road2
    y_road1=y_divider1+d1
    y_road2=y_divider2-d2
    plt.hlines(y_road1,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(y_road2,x,x+len,linestyles='solid',colors='black',lw=1)
    annonater(y_road1,y_divider1,x+600)
    annonater(y_road2,y_divider2,x+600)



    ##Drawing mid-road lines
    plt.hlines(y_divider1+d1/2,x,x+len,linestyles='dashed',colors='#ADD8E6',lw=1)
    plt.hlines(y_divider2-d2/2,x,x+len,linestyles='dashed',colors='#ADD8E6',lw=1)

    ##Get ofc line
    plt.hlines(y_divider2-d2/2-d3,x,x+len,linestyles='dashed',colors='red',lw=2)
    annonater(y_divider2-d2/2,y_divider2-d2/2-d3,x+400)



def get_roadside(d1=500,d2=500):
    global y_roadside1,y_roadside2
    y_roadside1=y_road1+d1
    y_roadside2=y_road2-d2
    plt.hlines( y_roadside1,x,x+len,linestyles='dashdot',colors='black',lw=1)
    plt.hlines(y_roadside2,x,x+len,linestyles='dashdot',colors='black',lw=1)
    annonater(y_roadside1,y_road1,x+300)    
    annonater(y_roadside2,y_road2,x+300)   

def outer_box(d=1200):
    
    yl=y_roadside1+d+100
    yr=y_roadside2-d-300
    plt.hlines(yl,x,x+len,linestyles='solid',colors='black',lw=1)
    plt.hlines(yr,x,x+len,linestyles='solid',colors='black',lw=1)       

def get_objects_roadside(d1=500,d2=700):
    yl=y_roadside1+d1
    yr=y_roadside2-d1   
    df=get_df()
    #print(df.index)
    #print(df,len(df.index))
    for i in df.index:
        #print(float(df['Chainage'][i]),d,df['RHS'][i])
        plt.text(float(df['Chainage'][i]),yr-d1,df['Road side objects(RHS)'][i],fontsize = 9,color='Black')
        plt.text(float(df['Chainage'][i]),yl+d1,df['Road side objects (LHS)'][i],fontsize = 9,color='Black')
        d=d2
        if df['Road side objects(RHS)'][i] == 'Forest':
            path = r"Forest.png"
            img = mpimg.imread(path)
            xx = df['Chainage'][i]+20
            yy = y_roadside2-d
            imagebox1 = OffsetImage(img,zoom=0.15)
            ab1 = AnnotationBbox(imagebox1, (xx, yy), frameon = False)
            ax.add_artist(ab1)
        elif df['Road side objects(RHS)'][i] == 'Pond':
            path = r"Pond.png"
            img = mpimg.imread(path)
            xx = df['Chainage'][i]+20
            yy = y_roadside2-d
            imagebox1 = OffsetImage(img,zoom=0.15)
            ab1 = AnnotationBbox(imagebox1, (xx, yy), frameon = False)
            ax.add_artist(ab1)

        if df['Road side objects (LHS)'][i] == "Forest":
            path = r"Forest.png"
            img=mpimg.imread(path)
            xx = df['Chainage'][i]+20
            yy = y_roadside1+d
            imagebox1 = OffsetImage(img, zoom = 0.15)
            ab1 = AnnotationBbox(imagebox1, (xx, yy), frameon = False)
            ax.add_artist(ab1)
        elif df['Road side objects (LHS)'][i] == "Pond":
            path = r"Pond.png"
            img=mpimg.imread(path)
            xx = df['Chainage'][i]+20
            yy = y_roadside1+d
            imagebox1 = OffsetImage(img, zoom = 0.15)
            ab1 = AnnotationBbox(imagebox1, (xx, yy), frameon = False)
            ax.add_artist(ab1)
        elif df['Road side objects (LHS)'][i] == "Farm":
            path = r"Farms.png"
            img=mpimg.imread(path)
            xx = df['Chainage'][i]+20
            yy = y_roadside1+d
            imagebox1 = OffsetImage(img, zoom = 0.15)
            ab1 = AnnotationBbox(imagebox1, (xx, yy), frameon = False)
            ax.add_artist(ab1)
        


def get_chainage(d=1400):
    df=get_df()
    yr=y_roadside2-d

    for i in df.index:
        plt.text(float(df['Chainage'][i]),yr,df['Chainage'][i],fontsize = 6,color='Black',rotation=90)

def get_culvert():
    df=get_df()
    for i in df.index:
        if df['Culvert'][i]=="Yes":
            tx1, ty1 = df['Chainage'][i]+20,y_roadside1
            tx2, ty2 = df['Chainage'][i]+20,y_roadside2

            imagebox1 = OffsetImage(mpimg.imread(r'Culvert.png'), zoom = 0.15)
            i1=OffsetImage(mpimg.imread(r'culvert_part.png'), zoom = 0.15)
            ab1 = AnnotationBbox(imagebox1, (tx1, ty1+55), frameon = False)
            a1=AnnotationBbox(i1, (tx1, ty1-170), frameon = False)

            imagebox2 = OffsetImage(mpimg.imread(r'Culvert2.png'), zoom = 0.15)
            i2=OffsetImage(mpimg.imread(r'culvert_part2.png'), zoom = 0.15)
            ab2 = AnnotationBbox(imagebox2, (tx2, ty2-55), frameon = False)
            a2=AnnotationBbox(i2, (tx2, ty2+170), frameon = False)
            plt.text(tx2+20, ty2-150,"Culvert",fontsize=5)
            ax.add_artist(ab1)
            ax.add_artist(a1)
            ax.add_artist(ab2)
            ax.add_artist(a2)
            
def get_bridge():
    df=get_df()
    for i in df.index:
        if df['Bridge Name'][i]=="Yes":
            tx1, ty1 = df['Chainage'][i]+20,y_roadside1
            tx2, ty2 = df['Chainage'][i]+20,y_roadside2

            imagebox1 = OffsetImage(mpimg.imread(r'Bridge2.png'), zoom = 0.15)
            i1=OffsetImage(mpimg.imread(r'Bridge_upper_part.png'), zoom = 0.15)
            ab1 = AnnotationBbox(imagebox1, (tx1, ty1+150), frameon = False)
            a1=AnnotationBbox(i1, (tx1, ty1-200), frameon = False)

            imagebox2 = OffsetImage(mpimg.imread(r'Bridge.png'), zoom = 0.15)
            i2=OffsetImage(mpimg.imread(r'Bridge_upper_part2.png'), zoom = 0.15)
            ab2 = AnnotationBbox(imagebox2, (tx2, ty2-150), frameon = False)
            a2=AnnotationBbox(i2, (tx2, ty2+200), frameon = False)
            plt.text(tx2+50, ty2-200,"Bridge\nw=",fontsize=5)
            ax.add_artist(ab1)
            ax.add_artist(a1)
            ax.add_artist(ab2)
            ax.add_artist(a2)

def get_serviceroad():
    df=get_df()
    for i in df.index:
        if df['Service Road Name'][i]=="Yes":
            tx1, ty1 = df['Chainage'][i]+20,y_road1
            tx2, ty2 = df['Chainage'][i]+20,y_road2

            if df['Service Road Side'][i]=="LHS":
                imagebox1 = OffsetImage(mpimg.imread(r'Culvert.png'), zoom = 0.15)
                #i1=OffsetImage(mpimg.imread(r'culvert_part.png'), zoom = 0.15)
                ab1 = AnnotationBbox(imagebox1, (tx1, ty1+55), frameon = False)
                #a1=AnnotationBbox(i1, (tx1, ty1-170), frameon = False)
                plt.text(tx1+20, ty1+120,"Service Road\nw=",fontsize=5)
                ax.add_artist(ab1)

            if df['Service Road Side'][i]=="RHS":
                imagebox2 = OffsetImage(mpimg.imread(r'Culvert2.png'), zoom = 0.15)
                #i2=OffsetImage(mpimg.imread(r'culvert_part2.png'), zoom = 0.15)
                ab2 = AnnotationBbox(imagebox2, (tx2, ty2-55), frameon = False)
                #a2=AnnotationBbox(i2, (tx2, ty2+170), frameon = False)
                plt.text(tx2+20, ty2-180,"Service Road\nw=",fontsize=5)
                ax.add_artist(ab2)

def coords(x=1980,y=3100):
        global len
        plt.text(x, y, 'N: XXX-XXX-XXX', fontsize = 9)
        plt.text(x, y-130, 'E: XXX-XXX-XXX', fontsize = 9)
        plt.text(x+len-5,y, 'N: XXX-XXX-XXX', fontsize = 9)
        plt.text(x+len-5, y-130, 'E: XXX-XXX-XXX', fontsize = 9)                        
            
def get_fixed_things(d=0):
    path =r"MS_box.png"
    imageList = [path, path]
    coordinates= [[2100,1500]]
    plt.text(2860,650,"To Mansar>>",fontsize=11,color='Blue')
    plt.text(2000,-800,"<< To Kurai",fontsize=11,color='Blue')
    plt.text(2250,-780,"<< NH-44 >>",fontsize=8,color='Blue')
    plt.text(2800,-780,"<< NH-44 >>",fontsize=8,color='Blue')
    plt.text(2750,450,"<< NH-44 >>",fontsize=8,color='Blue')
    plt.text(2200,450,"<< NH-44 >>",fontsize=8,color='Blue')
    plt.text(2500,490,"BT Road",fontsize=7,color='Green')
    plt.text(2500,-20,"<<Divider>>",fontsize=7,color='Black')
    plt.text(2600,-550,"BT Road",fontsize=7,color='Green')
    plt.text(2200,1250,"Gravel",fontsize=9,color='Green')
    plt.text(2700,1250,"Gravel",fontsize=9,color='Green')
    plt.text(2900,-1300,"Gravel",fontsize=9,color='Green')
    plt.text(2500,-1300,"Gravel",fontsize=9,color='Green')          



def get_soil(d=1600):
    df=get_df()
    for i in df.index:
        plt.text(float(df['Chainage'][i]),y_roadside2-d,df['Soil Types'][i],fontsize = 5,color='Black')

def draw_sld():
    try:
        get_road(lwidth,rwidth)  #Drawing roads (left +Right)
        get_roadside(lwidth,rwidth) #Drawing roadside lines (left + Right)
        get_divider(d_half) #Drawing divider on road (at half of divider width)
        get_objects_roadside() #Drawing road side objects (if images)
        get_ofc_line(d)
        get_culvert()
        #get_service_road(width,side,name)
        #get_fixed_things(coords)
        get_bridge(desc,coords,name)
        get_soil()
        get_chainage()

    except:
        print("All functions still not active")





fig=plt.figure(figsize=(3000,2000))   
ax = plt.gca()
ax.set_xlim(x-90, x+len+90)
plt.axis('off')
get_divider()
get_road()
get_roadside()
outer_box()
get_objects_roadside()
get_chainage()
get_culvert()
get_bridge()
get_soil()
get_serviceroad()
get_fixed_things()
coords()
#plt.hlines(3,0,1,linestyles='solid',colors='black',lw=1)
plt.show()















