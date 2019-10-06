N = int(input())

for i in range(N):
    print(' ' * (N-(N-i)) + '*'*(N-i))