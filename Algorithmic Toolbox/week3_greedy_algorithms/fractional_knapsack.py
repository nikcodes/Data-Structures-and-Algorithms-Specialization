# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    curr_w = 0
    # write your code here

    new = [[v/w,w] for v,w in zip(values,weights)]
    new.sort(reverse=1,key=lambda new:new[0])
    for rate,w in new:
    	if curr_w==capacity:
    		break
    	weight_chosen = min(capacity-curr_w,w)
    	value += weight_chosen * rate
    	curr_w += weight_chosen

    return value




n,capacity = [int(i) for i in input().split()]
weights=[]
values=[]
for _ in range(n):
	v,w = [int(i) for i in input().split()]
	values.append(v)
	weights.append(w)
ans = get_optimal_value(capacity,weights,values)
print('%.4f'%ans)