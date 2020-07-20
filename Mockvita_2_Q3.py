def count(i,j):
    h=max(i,j)
    l=min(i,j)
    p=(h,l)
    
    if p in mem:
        return mem[p]
    
    if(l==0):
        return 0
    
    if(l==1):
        return h
    
    choco=h//l
    side=h%l
    
    choco+=count(l,side)
    
    mem[p]=choco
    return choco
    
    
min_h=int(input())
max_h=int(input())
min_w=int(input())
max_w=int(input())
ans=0
mem={}
for i in range(min_h,max_h+1):
    for j in range(min_w,max_w+1):
        ans+=count(i,j)
        
#print(mem)            
print(ans,end='')
        
