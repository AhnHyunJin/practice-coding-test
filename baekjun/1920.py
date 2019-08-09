N = int(input())
arr_N = [int(x) for x in input().split()]
M = int(input())
arr_M = [int(x) for x in input().split()]

arr_N.sort()

def bin_search(arr,start,end, v):
    mid = int((end+start)/2)

    if start > end:
        print(0)
        return False
    else:
        if v > arr[mid]:
            start = mid + 1
        elif v == arr[mid]:
            print(1)
            return True
        elif v < arr[mid]:
            end = mid-1
        
    bin_search(arr, start, end, v)

for i in arr_M:
    ans = bin_search(arr_N, 0, N-1, i)
