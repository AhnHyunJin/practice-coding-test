import sys
n,m = map(int, sys.stdin.readline().split(' '))

_dict ={}

for i in range(0,n):
    tmp = list(str(input()))
    tmp = list(map(int, tmp))
    for j in range(0,m):
        key = str(i) + "," + str(j)
        _dict[key] = tmp[j]

print(_dict)