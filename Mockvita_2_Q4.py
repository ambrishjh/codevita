t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))[:n]
    x.insert(0,0)
    y=list(range(n+1))
    original=y
    count=0
    #print(x)
    #print(y)
    while True:
        z=[0]*(n+1)
        for j in range(1,n+1):
            z[x[j]]=y[j]
        count+=1
        #print(z)
        if(z==original):
            print(count,end='')
            break
        else:
            y=z
