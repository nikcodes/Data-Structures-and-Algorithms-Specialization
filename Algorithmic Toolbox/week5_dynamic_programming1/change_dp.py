# Uses python3

def f(i,remaining):
    if remaining==0:
        return 0
    if i==l:
        return float('infinity')

    if b[i][remaining]!=None:
        return b[i][remaining]

    m=float('infinity')
    for j in range(remaining//coins[i]+1):
        m=min(j + f(i+1,remaining-coins[i]*j), m)

    b[i][remaining]=m
    return m


n=int(input())
coins=[1,3,4]
l=len(coins)
b=[[None]*(n+1) for _ in range(l)]
print(f(0,n))



