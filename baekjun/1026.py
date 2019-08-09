N = int(input())
A = []
B = []

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

cp_B = B

A.sort()
cp_B.sort(reverse = True)

S =0
tmp=0
for i in range(N):
    tmp = A[i]*B[i]
    S += tmp
print(S)