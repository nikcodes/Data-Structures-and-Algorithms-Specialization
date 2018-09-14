# Uses python3

def f(e,a,n):
	if e in index:
		return index[e]
    i,j = 0,n-1

    while i<=j:
        m = (i + j) // 2
        index[a[m]]=m
        if a[m]==e:
            return m
        if a[m]<e:
            i=m+1
        else:
            j=m-1
    return -1

index={}
a=[int(i) for i in input().split()]
n=a[0]
elements=[int(i) for i in input().split()]
k=elements[0]

for e in elements[1:]:
    print(f(e,a[1:],n),end=' ')