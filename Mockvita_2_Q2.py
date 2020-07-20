n=int(input())                                                        #no fo 3-digit value
l=list(map(str,input().split()))[:n]                                  #3-digit integer value
#num=[]                                                               #bit score 
paire={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}                       #even array
pairo={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}                       #odd array
count=0
for key in l:
    n1=int(key[0])
    n2=int(key[1])
    n3=int(key[2])
    
    maxi=max(n1,n2,n3)
    mini=min(n1,n2,n3)

    
    temp=((maxi*11)+(mini*7))%100                                     #Calculation of bit score
    #num.append(temp)
    temp=temp//10                                                     #most sig
    if(count%2==0):                                                   #even
        paire[temp]+=1
    else:                                                             #odd
        pairo[temp]+=1
    count+=1
sum=0
#print(paire)
#print(pairo)
for key in range(10):
    if(paire[key]>2 or pairo[key]>2):
        sum+=2
    else:
        if(paire[key]==2):
            sum+=1
        if(pairo[key]==2):
            sum+=1
        
#print(num)
print(sum)
