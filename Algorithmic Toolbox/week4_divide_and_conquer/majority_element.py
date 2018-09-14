# Uses python3
from sys import exit
from collections import defaultdict

n=int(input())
m=n/2
a=[int(i) for i in input().split()]
d=defaultdict(lambda:0)
for e in a:
    d[e]+=1
    if d[e]>m:
        print(1)
        exit()

print(0)
