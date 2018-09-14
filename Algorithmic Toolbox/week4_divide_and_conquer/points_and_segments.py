# Uses python3

def bsearch(e):
    i=0
    j=n-1
    while i<=j:
        m=(i+j)//2

        if a[m][0]==e:
            if e<a[m+1][0]:
                return openranges[m]
            elif e==a[m+1][0]:
                l=m+1

        elif a[m-1][0]==e:
            if e<a[m][0]:
                return openranges[m-1]
            elif e==a[m][0]:
                l=m

        else:
            if e>a[m][0]:
                i=m+1
            elif e<a[m][0]:
                j=m-1
    return 0



s,p=[int(i) for i in input().split()]
a=[]
for _ in range(s):
    l,r=[int(i) for i in input().split()]
    a.extend([[l,'b'],[r,'e']])
points=[int(i) for i in input().split()]


openranges=[1]
for n,t in a[1:]:
    if t=='b':
        openranges.append(openranges[-1]+1)
    else:
        openranges.append(openranges[-1]-1)

a.sort()
n=len(a)
for e in points:
    print(bsearch(e),end=' ')