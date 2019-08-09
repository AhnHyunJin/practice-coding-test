import math as m

from decimal import *


N,K = input().split(" ")

N = int(N)
K = int(K)
arr = []    
pow_arr = []
dolls = input()
people = dolls.split(" ")

for i in people:
    i = float(i)
    i = Decimal(i)
    arr.append(i)
    pow_arr.append(pow(i,2))


partial_sum = []
pow_partial_sum=[]
min = 9999999

for i in range(0,N):
    tmp = 0
    tmp2 = 0
    
    for j in range(0,i+1):
        tmp = Decimal(arr[j]) + Decimal(tmp)
        tmp2 = Decimal(pow_arr[j]) +Decimal(tmp2)
    partial_sum.append(tmp)
    pow_partial_sum.append(tmp2)

for i in range(K-1,N):
    mean = partial_sum[i] / Decimal((i+1))
    pow_mean = pow_partial_sum[i]/Decimal(i+1)
    var = pow_mean - Decimal(pow(mean,2))
    sigma = Decimal(var).sqrt()
        
    if min>sigma:
        min = sigma

for i in range(0,N):
    for j in range(0,N):
        if (i-j) < K:
            break
        else:               
            mean = (partial_sum[i] - partial_sum[j]) / Decimal(i-j)
            pow_mean = (pow_partial_sum[i] - pow_partial_sum[j]) / Decimal(i-j)
            var = pow_mean - Decimal(pow(mean,2))
            sigma = Decimal(var).sqrt()
            
            if min>sigma:
                min = sigma

print(round(min,11))
