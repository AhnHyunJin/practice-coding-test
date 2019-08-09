from collections import deque
import sys

#N = 최고차항
N = int(input())

q = [0]*(N+1)

q = [x for x in map(int, sys.stdin.readline().split())]


dim = 0
sum_of_X = N
sum_of_mul = N-1
sum_of_plus = N
answer = 0

#계수 누르는 갯수
def count_number(n,dim):
    cnt = 1
    
    if dim == N:
        return 0
        
    while n >= 10:
        cnt +=1
        n %= 10

    return cnt


while q:
    tmp = q.pop()
    if tmp == 0:
        sum_of_plus -= 1
        
    else:
        #계수
        answer += count_number(tmp,dim)
    dim+=1

#마지막 + 은 등호(=)의 갯수
answer = answer + sum_of_mul + sum_of_plus + sum_of_X + 1
print(answer)