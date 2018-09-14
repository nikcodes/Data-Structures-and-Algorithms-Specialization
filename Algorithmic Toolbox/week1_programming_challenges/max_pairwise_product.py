# python3


n=int(input())
a=[int(i) for i in input().split()]

def swap(i,n):
    ind=i
    largest=a[i]
    if 2*i+1<n and a[2*i+1]>a[i]:
        largest=a[2*i+1]
        ind=2*i+1

    if 2*i+2<n and a[2*i+2]>largest:
        ind=2*i+2

    if i==ind:
        return 

    a[i],a[ind] = a[ind],a[i]
    swap(ind,n)

if n==2:
    print(a[0]*a[1])

else:

    for i in range(n//2-1,-1,-1):
        swap(i,n)

    print(a[0] * max(a[1],a[2]))
