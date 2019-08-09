import sys
def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a,b):
    return a * b/gcd(a,b)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x,y = map(int, sys.stdin.readline().split())
        if x > y :
            print(int(lcm(x,y)))
        else:
            print(int(lcm(y,x)))
