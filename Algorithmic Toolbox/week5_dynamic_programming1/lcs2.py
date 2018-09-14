#Uses python3

def f(i,j):
    if i>n-1 or j>m-1:
        return 0

    if d[i][j]!=None:
        return d[i][j]

    if a[i]==b[j]:
        ans=1+f(i+1,j+1)
        d[i][j]=ans
        return ans

    ans=max(f(i,j+1),f(i+1,j),f(i+1,j+1))
    d[i][j] = ans

    return ans

n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]
d=[[None]*m for _ in range(n)]
print(f(0,0))