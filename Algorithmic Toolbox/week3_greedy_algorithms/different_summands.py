# Uses python3

n=int(input())
if n==1:
    print(1)
    print(1)

elif n==2:
    print(1)
    print(2)

else:
    # a=[1,2]
    a=[]
    remaining = n
    f,s = 1,2
    while 1:
        if f+s<=remaining:
            a.append(f)
            remaining-=f
            f,s = s,s+1
        else:
            a.append(remaining)
            ans=f
            break

    print(ans)
    for e in a:
        print(e,end=' ')