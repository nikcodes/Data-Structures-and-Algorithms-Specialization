# Uses python3
import sys

def lcm_naive(a, b):
    p=a*b
    while b:
    	a,b = b,a%b
    return p//a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

