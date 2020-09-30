from copy import deepcopy
try:
    n=int(input())
    l=list(map(int,input().split()))
    c=deepcopy(l)
    l.insert(0,0)
    ans=[str(1)]
    l2=[]
    i=0
    
    while(i<=n):
            t=l[int(ans[-1])]
            if(t in c):
                ans.append(str(t))
                c.remove(t)
            else:
                l2.append(ans)
                if(c!=[]):
                    i=min(c)
                    ans=[str(i)]
                else:
                    break
    l2.append(ans)
    if(l2[-2]==l2[-1]):
            l2.remove(l2[-1])
    print(len(l2))
    for i in l2:
            print(" ".join(i))

except Exception:
    pass