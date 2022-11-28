import pandas as pd



data = {'from': [10,20,30,50,70,100,120,150,200],
        'to': [20,30,40,60,80,120,150,190,260]}
# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data)
print(df)

sum=0
i=0
print(len(df))
while i<len(df)-1:
    temp=df['to'][i]-df['from'][i]
    for j in range(i,len(df)-1):
        print("j is",j,"From",df['from'][j],"to",df['to'][j],"temp",temp)
        if df['from'][j+1]==df['to'][j]:
            temp+=df['to'][j+1]-df['from'][j+1]
        else:
            i=j+1
            print(i)
            if temp>50:
                temp-=50
            else:
                temp=0    
            sum+=temp
            print("temp is",temp,"sum is",sum)   
            temp=0 
            break
    
    if temp>50:
        temp-=50
    else:
        temp=0    
    sum+=temp
    temp=0
    
    



print(sum)
