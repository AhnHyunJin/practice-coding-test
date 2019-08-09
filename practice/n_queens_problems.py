result = 0
col = [-1] * 15
def promissing(i):
    global col
    for j in range(i):
        if col[j] == col[i] or abs(col[i]- col[j]) == i-j:
            return False
    return True

def nqueen(i):
    global result
    global col
    if i ==N:
        result +=1

    else:
        for j in range(N):
            col[i] = j
            if promissing(i):
                nqueen(i+1)

N = int(input())
nqueen(0)


print(result)