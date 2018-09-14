# Uses python3

def f(i,j):
    M=float('-infinity')
    m=float('infinity')
    for k in range(i,j):
        w=eval(str(maxi[i][k]) + b[k] + str(maxi[k+1][j]))
        x=eval(str(maxi[i][k]) + b[k] + str(mini[k+1][j])) 
        y=eval(str(mini[i][k]) + b[k] + str(maxi[k+1][j])) 
        z=eval(str(mini[i][k]) + b[k] + str(mini[k+1][j])) 
        M=max(w,x,y,z,M)
        m=min(w,x,y,z,m)

    maxi[i][j]=M
    mini[i][j]=m
    return M,m

op={'+','-','*','/'}
s=input()
a=[]
b=[]
for e in s:
    if e not in op:
        a.append(int(e))
    else:
        b.append(e)

# a=[int(e) for e in s if int(e) in rang]
# b=[e for e in s if e not in rang]

n=len(a)

maxi=[[None]*n for _ in range(n)]
mini=[[None]*n for _ in range(n)]

for i in range(n):
    mini[i][i]=a[i]
    maxi[i][i]=a[i]

for k in range(1,n):
    for i in range(n-k):
        j=i+k
        M,m=f(i,j)

print(maxi[0][n-1])