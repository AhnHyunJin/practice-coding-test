sum = 0
for _ in range(0,5):
    
    score = int(input())
    if score <40 : 
        score = 40
    sum += score
avg = int(sum/5)
print(avg)