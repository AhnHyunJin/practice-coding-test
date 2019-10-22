import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
a1, b1, a2, b2 = map(int, sys.stdin.readline().split(' '))

def chk_state(x1,x2,a1,a2):    
    if x1 > a2 or x2 < a1:
        state = "NULL"
        return state
    elif a2 == x1 or x2 == a1:
        state = "POINT"
        return state
    else:
        state = "LINE"
        return state

x_state = chk_state(x1,x2,a1,a2)
y_state = chk_state(y1,y2,b1,b2)


if x_state == "NULL" or y_state == "NULL":
    print("NULL")

elif x_state == "POINT":
    if y_state == "POINT":
        print("POINT")
    else:
        print("LINE")
else:
    if y_state == "POINT":
        print("LINE")
    else:
        print("FACE")