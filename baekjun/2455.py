ret = 0
ans = 0

for _ in range(4):    
    o,i = input().split(' ')
    o = int(o)
    i = int(i)
    
    ret -= o
    ret += i

    ans = max(ret, ans)

print(ans)
