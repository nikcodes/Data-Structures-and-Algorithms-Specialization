# # Uses python3



def get_fibonacci_huge_optimized(n, m):
    d={}
    f,s = 0,1
    a=[0]
    period=None

    for i in range(2,n+1):
        if (f,s) in d:
            period = i-2
            break
        d[(f,s)]=1
        a.append(s)
        f,s = s,(f+s)%m

    # return f'pattern length is {period}'

    if period:
        return a[n%period]
    return s
    



n,m = [int(i) for i in input().split()]
print(get_fibonacci_huge_optimized(n, m))