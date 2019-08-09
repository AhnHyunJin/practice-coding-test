def com_num(a,b):
    cycle_arr = []
    cycle =0
    if(a>10):
        a = a % 10

    if a == 0:
        return 10
    #cycle과 exponent의 관계를 제대로 정의할 수 있으면 좋을듯.
    else:
        base = a
        cycle = 1
        cycle_arr.append(base)
        while ( (a * base) % 10 ) != base:
            a = (a * base) % 10
            cycle_arr.append(a)
            cycle += 1
        
        res = b % cycle        
        ret = cycle_arr[res-1]
    return ret

if __name__ == '__main__':
    N = int(input())
    ret = []
    for i in range(N):
        a,b = input().split(' ')
        a = int(a)
        b = int(b)
        ret.append(com_num(a,b))
    for i in ret:
        print(i)
    
        


