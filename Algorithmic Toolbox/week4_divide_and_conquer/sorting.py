# Uses python3

from collections import defaultdict

n=int(input())
a=[int(i) for i in input().split()]

d=defaultdict(lambda:0)
b=[]
for e in a:
    d[e]+=1
    if d[e]==1:
        b.append(e)

for e in sorted(b):
    print((str(e)+' ')*d[e],end='')