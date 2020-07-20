n=int(input())                            # number of strings
b=input()                                 #bride string
g=input()                                 #groom string cin>>s s[1]
gcount={"r":0,"m":0}                      # int r=0,m=0; gcount["r"]==0
for key in g:                             #groom traversing bride=rrmm groom=mrmr 
    gcount[key]+=1                        #if(key=="r")r++ ; else m++ key="r"or"m"

for key in b:
    if(gcount[key]!=0):                   #input "r" groom r!=0 similarly "m"
        gcount[key]-=1
    else:
        break
sum=gcount["r"]+gcount["m"]
print(sum,end='')
