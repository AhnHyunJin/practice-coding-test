T = int(input())

for _ in range(T):
    ans = ""
    R, S = input().split(" ")
    for c in S:
        for _ in range(int(R)):
            ans += c
    print(ans)