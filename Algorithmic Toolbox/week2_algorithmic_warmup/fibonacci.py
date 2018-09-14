# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    a=[0,1]
    for i in range(2,n+1):
    	a.append(a[-1]+a[-2])
    return a[-1]

n = int(input())
print(calc_fib(n))
