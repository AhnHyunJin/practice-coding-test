

def cal_change(coin_count, change, coin):
    while change >= coin:
        coin_count += 1
        change -= coin        
    return coin_count, change



if __name__ == '__main__':
    price = int(input())
    change = 1000-price
    
    coin_count = 0
    coin = [500,100,50,10,5,1]

    while change > 0:
        if change >= 500:        
            
            coin_count, change = cal_change(coin_count,change, coin[0])        

        elif change>=100:
            coin_count, change = cal_change(coin_count,change,coin[1])
            

        elif change>=50:
     
            coin_count, change = cal_change(coin_count,change, coin[2])   
          
            
        elif change>=10:
            coin_count, change = cal_change(coin_count,change, coin[3])
        elif change>=5:
            coin_count, change = cal_change(coin_count,change, coin[4])
        else:    
            
            coin_count += change
                
            change = 0

    print(coin_count)