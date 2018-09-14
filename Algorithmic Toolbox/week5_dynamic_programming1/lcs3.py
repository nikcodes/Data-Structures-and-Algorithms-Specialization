#Uses python3

def f(i,j,k):
    if i>n-1 or j>m-1 or k>l-1:
        return 0

    if d[i][j][k]!=None:
        return d[i][j][k]

    if a[i]==b[j]==c[k]:
        ans = 1 + f(i+1,j+1,k+1)

    else:
        ans = max(f(i,j,k+1), f(i,j+1,k+1), f(i,j+1,k), f(i+1,j,k+1), f(i+1,j+1,k+1), f(i+1,j+1,k),f(i+1,j,k))

    d[i][j][k]=ans
    return ans


n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]
l=int(input())
c=[int(i) for i in input().split()]

d=[[[None]*l for _ in range(m)] for _ in range(n)]

print(f(0,0,0))