# Uses python3
import sys
from collections import defaultdict
n=int(input())
if n==1:
    print(0)
    print(1)
    sys.exit()
ind=defaultdict(lambda:[])
a=[0,0,1,1]

for i in range(4,n+1):
    m=a[i-1]

    if i%2==0 and a[i//2]<m:
        m=a[i//2]

    if i%3==0 and a[i//3]<m:
        m=a[i//3]

    a.append(m+1)

for i in range(1,n+1):
    ind[a[i]].append(i)

final=[n]
num=n

for cur in range(a[-1],0,-1):
    for e in ind[cur-1]:
        if e==num-1:
            num=num-1
            final.append(e)
            break
        elif num%2==0 and e==num//2 :
            num=num//2
            final.append(e)
            break

        elif num%3==0 and e==num//3:
            num//=3
            final.append(e)
            break



print(a[-1])
for e in final[::-1]:
    print(e,end=' ')

