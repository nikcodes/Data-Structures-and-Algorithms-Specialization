# Uses python3
from operator import itemgetter

n=int(input())
a=[]
for i in range(n):
    s,e=[int(i) for i in input().split()]
    a.extend([[s,i,'b'],[e,i,'e']])

a.sort(key=itemgetter(0,2))

due={}
final=[]
ans=0

for time,index,type in a:
    if type=='e':
        if index in due:
            final.append(time)
            ans+=1
            due={}

    else:
        due[index]=1


print(ans)
for e in final:
    print(e,end=' ')






