t=int(input())
for i in range(t):
    p=input()
    s=input()
    letter={}
    for j in range(len(p)):
        letter[p[j]]=j
    a=[]
    for words in s:
        a.append(letter[words])
    a.sort()
    ans=""
    for j in a:
        ans+=p[j]
    print(ans,end='') 
