#Uses python3

from functools import cmp_to_key
#
#
def cmp(x, y):
    if int(str(x)+str(y))>int(str(y)+str(x)):
        return -1
    elif int(str(x)+str(y))<int(str(y)+str(x)):
        return 1
    else:
        return 0




n=int(input())
nums=[int(i) for i in input().split()]
nums.sort(key=cmp_to_key(cmp))
for e in nums:
    print(e,end='')




