# Uses python3

w,n=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

b=[[None]*n for _ in range(w+1)]

for i in range(w+1):
	if i>=a[0]:
		b[i][0]=a[0]
	else:
		b[i][0]=0
for i in range(n):
	b[0][i]=0

for i in range(1,w+1):
	for j in range(1,n):
		b[i][j] = b[i][j-1]
		if a[j]<=i:
			b[i][j] = max(b[i][j], a[j] + b[i-a[j]][j-1])

print(b[-1][-1])