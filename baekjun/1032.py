N = int(input())
filename = [None] * N
for i in range(N):
    filename[i] = input()

filelen = len(filename[0])
pattern =  ""
if N !=1:
    for i in range(filelen):
        for j in range(1,N):
            pivot = filename[0][i]        
            if pivot != filename[j][i]:
                pattern += "?"
                break
            else:
                if j == N-1:
                    pattern += pivot
else:
    print(filename[0])
print(pattern)