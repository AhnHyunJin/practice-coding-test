import sys

x,y = map(int, sys.stdin.readline().split())

x_dict = { 1: 31, 2: 28, 3: 31, 4: 30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
y_dict = {1:'MON', 2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',0:'SUN'}

date = 0

for month in range(1,x):    
    date += x_dict[month]

date = (date + y) %7

print(y_dict[date])