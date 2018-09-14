# Uses python3

def msort(l,r):
    global ans
    if l==r:
        return

    m=(l+r)//2
    msort(l,m)
    msort(m+1,r)

    i,j = l,m+1
    b=[]

    while i<=m and j<=r:
        if a[i]<a[j]:
            b.append(a[i])
            i+=1
        elif a[i]>a[j]:
            ans+=m-i+1
            b.append(a[j])
            j+=1
        else:
            b.append(a[i])
            i+=1


    a[l:r+1]=b+a[i:m+1]+a[j:r+1]


n=int(input())
a=[int(i) for i in input().split()]

ans=0
msort(0,n-1)
print(ans)


