# Uses python3
import sys

def last_digit(n):


    f,s = 0,1
    d={}
    a=[f]
    summ=1
    period=None
    for i in range(2,n+1):
        if (f,s) in d:
            period=i-2
            break
        if (f,s) == (0,1):
            d[(f,s)]=1
        
        a.append(s)
        f,s = s,(f+s)%10
        summ+=s

    if period:
        summ-=1

    
    return period,summ%10,a



def fibonacci_sum_optimized(n):
    if n == 1:
        return n
    if n<=0:
        return 0

    period,firstsum,a = last_digit(n)
    if period:
        final_sum = (n//period*firstsum)%10 + sum(a[:(n%period)+1])%10
        return final_sum%10
    return firstsum



m,n = [int(i) for i in input().split()]
msum=fibonacci_sum_optimized(m-1)
nsum=fibonacci_sum_optimized(n)
ans=nsum-msum
if ans<0:
    ans+=10
print(ans)