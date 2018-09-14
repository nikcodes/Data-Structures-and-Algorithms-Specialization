# Uses python3

n=int(input())
a=[int(i) for i in input().split()]

def f(x,y,z,i):
    if i==n:
        if x==y==z:
            return 1
        else:
            return 0

    return f(x+a[i],y,z,i+1) or f(x,y+a[i],z,i+1) or f(x,y,z+a[i],i+1)

print(f(0,0,0,0))