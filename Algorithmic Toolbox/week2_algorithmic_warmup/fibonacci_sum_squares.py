# Uses python3

def lastf(n):
    d={}
    f,s = 0,1
    a=[f]
    period = None
    for i in range(2,n+1):
        if (f,s) in d:
            period=i-2
            break
        d[(f,s)]=1
        a.append(s)
        f,s = s,(f+s)%10

    if period:
        return a[n%period]
    return s


def square(n):
    if n<=1:
        return n
    lastn = lastf(n)
    lastn1 = lastf(n-1)
    return (lastn * (lastn+lastn1))%10

n=int(input())
print(square(n))