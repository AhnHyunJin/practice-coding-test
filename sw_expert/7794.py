from decimal import *
T = int(input())

one_percent = []
two_percent = []
three_percent= []
all_price = []
discounted_price = Decimal(0)

for test in range(T):
    N , C = input().split()
    N = int(N)
    C = int(C)
    discounted_price = Decimal(C)
    one_percent.clear()
    two_percent.clear()
    three_percent.clear()
    all_price.clear()
    
    for _ in range(N):
        coupon_price, coupon_discount = input().split()
        coupon_price = Decimal(coupon_price)
        coupon_discount = Decimal(coupon_discount)
        if Decimal(coupon_discount) / Decimal(100) * C > coupon_price:
            if coupon_discount == 1:
                one_percent.append(coupon_price)
            elif coupon_discount == 2:
                two_percent.append(coupon_price)
            elif coupon_discount == 3:
                three_percent.append(coupon_price)
    
    if one_percent:
        for price in one_percent:
            discounted_price = Decimal(discounted_price) * Decimal(0.99)
            all_price.append(price)
    if two_percent:
        for price in two_percent:
            discounted_price = Decimal(discounted_price) * Decimal(0.98)
            all_price.append(price)
    if three_percent:    
        for price in three_percent:
            discounted_price = Decimal(discounted_price) * Decimal(0.97)            
            all_price.append(price)
            
    if all_price:
    	for x in all_price:
        	discounted_price  += Decimal(x)
    
    
    print("#"+ str(test+1) ,round(min(C, discounted_price), 7))