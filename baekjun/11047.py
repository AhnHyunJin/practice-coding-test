import sys
N,K= map(int, sys.stdin.readline().split())

count = 0
money_type = []
for _ in range(N):
    tmp = int(input())
    money_type.append(tmp)

money_type.sort(reverse = True)


for money in money_type:
    
    money = int(money)
    tmp = int(K / money)
    count += tmp
    K = K % money
    
print(count)