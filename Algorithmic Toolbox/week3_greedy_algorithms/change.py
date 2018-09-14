#Uses python3

m=int(input())
a=[10,5,1]
ans=0

for e in a:
	ans += m//e
	m=m%e

print(ans)