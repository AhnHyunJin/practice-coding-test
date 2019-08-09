N = int(input())
A = [int(x) for x in input().split()]


A.sort()

if len(A) % 2 ==0:
    ans = A[0] * A[N-1]
else:
    mid = int(len(A)/2)
    ans = A[mid]*A[mid]

print(ans)