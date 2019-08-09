if __name__ == '__main__':
    N = input()
    ret_list = []

    while(True):        
        a = int(int(N) / 10)
        b = int(int(N) % 10)
        tmp = a + b

        tmp = str(b) + str(tmp % 10)        

        if tmp in ret_list:
            print(len(ret_list))
            break

        ret_list.append(tmp)
        N = str(tmp)