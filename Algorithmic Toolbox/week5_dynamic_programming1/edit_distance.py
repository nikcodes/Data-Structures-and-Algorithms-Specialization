# Uses python3

def f(i,j):

    if i==n:
        return m-j
    if j==m:
        return n-i

    if d[i][j]!=None:
        return d[i][j]

    if a[i]==b[j]:
        ans=f(i+1,j+1)
    else:
        ans = 1 + min(f(i+1,j),f(i,j+1),f(i+1,j+1))

    d[i][j]=ans
    return ans


a=input()
b=input()
n=len(a)
m=len(b)
d=[[None]*m for _ in range(n)]

print(f(0,0))