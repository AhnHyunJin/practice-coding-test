s = input().upper()
s = sorted(s)

count = 1
_max = 0

pre = s.pop()



while s:    
    cur = s.pop()
    print("pre : ", pre, "cur : ", cur)

    if pre == cur:
        count += 1
        
        
        
    else:        
        if count == _max:            
            ans = "?"
        elif count > _max:
            _max = count
            ans = pre
        count = 1
        pre = cur
        
    

print(ans)