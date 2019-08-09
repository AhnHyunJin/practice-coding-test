import sys

A,B = map(str, sys.stdin.readline().split())

len_A = len(A)
len_B = len(B)
tmp = 0
min_val = 999
dif = 0

for i in range(len_B - len_A + 1):
    #dif = len_B - len_A    
    tmp_B = B[i:i+len_A]
    
    for j in range(len_A):  
        if tmp_B[j] != A[j]:
            dif +=1
            
    min_val = min(min_val, dif)
    dif = 0
        
print(min_val)