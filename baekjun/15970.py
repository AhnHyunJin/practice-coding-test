import sys

point = {

}

N = int(input())
ans = 0

for _ in range(N):
    offset, color = map(int, sys.stdin.readline().split(' '))    
    
    
    if color not in point.keys():
        point[color] = [offset]
    else:
        point[color].append(offset)

for i in point.keys():
    points = point[i]
    
    points.sort()
    
    for j in range(0,len(points)):
        if j == len(points) -1:
            ans += (points[j] - points[j-1])
        else:
            cur_val = points[j]
            next_val = points[j+1]
            if j ==0:
                min_val = next_val - cur_val
                ans += min_val
                
                continue
            
            tmp = next_val - cur_val
            min_val = min(min_val, tmp)
            
            ans+= min_val
            min_val = tmp

print(ans)


# p = {
#     1 : 2
# }

# if 2 not in p.keys():
#     p[2] = [3]

# p[1] = [p[1]]
# print(p[2])