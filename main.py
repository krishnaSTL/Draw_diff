import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as image


class road_param:
    def __init__(self,pos_x,pos_y,length=10,ofc_h=-8.5,RHS_h=9,LHS_h=9,div_h=2,RHS_extra_h=5,LHS_extra_h=5):
        self.RHS_h=RHS_h
        self.LHS_h=LHS_h
        self.div_h=div_h
        self.RHS_extra_h=RHS_extra_h
        self.LHS_extra_h=LHS_extra_h
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.ofc_h=ofc_h
        self.length=1


    def chainage(self):
        df=pd.read_excel(r"C:\Users\Aditya.gupta\Documents\Untitled 1.xls")
        for i in range(0,len(df.index)):
            print(self.pos_x+float(df['Chainage'][i]),2,df['RHS'][i])
            if ~pd.isna(df['RHS'][i]):
                plt.text(float(df['Chainage'][i]),-12,df['RHS'][i],fontsize = 9,color='Black')
            if ~pd.isna(df['LHS'][i]): 
                plt.text(float(df['Chainage'][i]),19.2,df['LHS'][i],fontsize = 9,color='Black')

    def coords(self,y,x):
        x=self.pos_x
        y=self.pos_y+(self.div_h/2)+(self.LHS_h)+(self.LHS_extra_h)+3
        plt.text(x, y, 'N: XXX-XXX-XXX', fontsize = 9)
        plt.text(x, y-1, 'E: XXX-XXX-XXX', fontsize = 9)
        plt.text(x+self.length-0.05,y, 'N: XXX-XXX-XXX', fontsize = 9)
        plt.text(x+self.length-0.05, y-1, 'E: XXX-XXX-XXX', fontsize = 9)

    def annonater(self,y1,y2,x,text=""):
        plt.annotate(
        '',xy=(x, y1), xycoords='data',
        xytext=(x, y2), textcoords='data',color='Red',
        arrowprops=dict(arrowstyle= '<->',color='red'))
        plt.annotate(
        abs(y1-y2), xy=(x, (y1+y2)/2), xycoords='data',color='Red'
        #xytext=(5, 0), textcoords='offset points'
        )
        
        plt.text(x+0.4,(y1+y2)/2,text,fontsize=7,color='green')
           

    def draw(self):

        fig=plt.figure(figsize=(25,5.5))    
        l=self.length
        
        ##Chainage
        self.chainage()
        
        #Divider lines LHS+RHS
        y1=self.pos_y+(self.div_h/2)
        y2=self.pos_y-(self.div_h/2)
        x=self.pos_x
        plt.hlines(y1,x,x+l,linestyles='solid',colors='black',lw=1)
        plt.hlines(y2,x,x+l,linestyles='solid',colors='black',lw=1)
        self.annonater(y1,y2,x+.2,"Divider")
        #self.annonater(y1,y2,x-.2,"<<Divider>>")
        
        #Road Boundary LHS
        y1=self.pos_y+(self.div_h/2)+(self.LHS_h)
        y2=self.pos_y+(self.div_h/2)
        x=self.pos_x
        plt.hlines(y1,x,x+l,linestyles='solid',colors='black',lw=1)
        self.annonater(y1,y2,x+0.1,"BT Road")
        

        #Road Boundary LHS mid
        plt.hlines(self.pos_y+(self.div_h/2)+(self.LHS_h/2),self.pos_x,self.pos_x+l,linestyles='dashed',colors='blue',lw=1)

        #Road side LHS
        y1=self.pos_y+(self.div_h/2)+(self.LHS_h)+(self.LHS_extra_h)
        y2=self.pos_y+(self.div_h/2)+(self.LHS_h)
        x=self.pos_x
        plt.hlines(y1,x,x+l,linestyles='dashdot',colors='black',lw=1)
        self.annonater(y1,y2,x+0.2,"Gravel")
        self.coords(x,y1+1)
        

        #Road Boundary RHS
        y1=self.pos_y-(self.div_h/2)-(self.RHS_h)
        y2=self.pos_y-(self.div_h/2)
        x=self.pos_x
        plt.hlines(y1,x,x+l,linestyles='solid',colors='black',lw=1)
        self.annonater(y1,y2,x+0.1,"BT Road")
        
        #Road Boundary RHS mid
        plt.hlines(self.pos_y-(self.div_h/2)-(self.RHS_h/2),self.pos_x,self.pos_x+l,linestyles='dashed',colors='blue',lw=1)

        #Road side RHS
        y1=self.pos_y-(self.div_h/2)-(self.RHS_h)-(self.RHS_extra_h)
        y2=self.pos_y-(self.div_h/2)-(self.RHS_h)
        plt.hlines(y1,x,x+l,linestyles='dashdot',colors='black',lw=1)
        self.annonater(y1,y2,x+0.2,"Gravel")

        #OFC Line
        y1=self.pos_y-(self.div_h/2)-(self.RHS_h/2)+(self.ofc_h)
        y2=self.pos_y-(self.div_h/2)-(self.RHS_h/2)
        x=self.pos_x
        plt.hlines(self.pos_y-(self.div_h/2)-(self.LHS_h/2)+(self.ofc_h),x,x+l,linestyles='dashed',colors='#FF00FF',lw=2)
        self.annonater(y1,y2,x)
        plt.text(x+0.3,y1+0.2,"Proposed OFC Route",fontsize=7,color='#FF00FF')


        ##Extra labels
        y1=self.pos_y-(self.div_h/2)-(self.RHS_h/2)
        y2=self.pos_y-(self.div_h/2)-(self.RHS_h)
        x=self.pos_x
        plt.text(x+0.1,(y1+y2)/2,"<<To Kurai",color="#00008B",fontsize=11,weight='bold')
        y1=self.pos_y+(self.div_h/2)+(self.LHS_h/2)
        y2=self.pos_y+(self.div_h/2)+(self.LHS_h)
        x=self.pos_x
        plt.text(x+self.length-0.2,(y1+y2)/2,"To Mansar>>",color="#00008B",fontsize=11,weight='bold')

        y1=self.pos_y+(self.div_h/2)+(self.LHS_h/2)
        y2=self.pos_y-(self.div_h/2)-(self.RHS_h/2)
        x=self.pos_x+(self.length/2)
        plt.text(x-.3,y1+0.5,"<<NH-44>>",color="#00008B",fontsize=10)
        plt.text(x-.3,y2+0.5,"<<NH-44>>",color="#00008B",fontsize=10)
        
        
        ##Showing route marker on plot
        rm=image.imread(r"C:\Users\Aditya.gupta\Desktop\Fun Projects\Draw_diff\rc.jpg.png")
        #img = rm.resize((50, 40))
        x1=self.pos_x
        y1=self.pos_y+(self.div_h/2)+(self.LHS_h)
        fig.figimage(rm,x*125, y1*44+5)
        plt.text(x1,y1+0.2,"MS-62",color="#000000",fontsize=9)
        fig.figimage(rm,(x+self.length)*462, y1*44+5)
        plt.text(x1+self.length-0.04,y1+0.2,"MS-63",color="#000000",fontsize=9)       #Annotation box for solar pv logo
        #Container for the imagebox referring to a specific position *xy*.
        #plt.axis('off')
        plt.xlabel("Chainage (in Kms)")

        
        



Road1=road_param(2,8)
print(Road1.pos_y)
Road1.draw()
plt.gca().axes.get_yaxis().set_visible(False)
#df=pd.read_excel(r"C:\Users\Aditya.gupta\Documents\Untitled 1.xls")
#print(df)
plt.show()



