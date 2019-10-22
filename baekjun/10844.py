# -*- coding: utf-8 -*- 

#dp를 이용해서 풀 때, 점화식을 꼭 생각해보자. 다시 풀어볼 것.
#해당 숫자가 나올 수 있는 경우의 수는?? 점화식을 세울 때 기준을 잘 잡아야 할 것.
d= {
    0: [1],
    1: [0,2],
    2: [1,3],
    3: [2,4],
    4: [3,5],
    5: [4,6],
    6: [5,7],
    7: [6,8],
    8: [7,9],
    9: [8]
}


N = int(input())

#아래의 과정은 모두 똑같다 그러므로 함수 처리를 하도록 하자
#num에 첫째 자리수를 전달한다. 첫째자리 수는 1~9이므로, 반복문을 통해서 sol 함수를 돌리도록 한다
sum = 0


def sol(num,N):
    #n1 = [num]
    #아래 반복문의 연산은 2,3,4,....N까지의 자릿수동안 반복되는 연산이다 이를 반복문 하나로 합칠 수 있겠는가?
    #알아야할 것은 무엇인가?? 아래는 N = 4인 경우이므로, N 이 몇인지 알아야 한다 그러므로 함수에서 N 을 전달받도록 하자
    
    #반복문이 진행될 수록 다음 자릿수로 넘어가야 한다 n1 -> n2 ->n3 이를 어떻게 해결 할 것인가??
    #임시 배열 tmp 를 이용할 수 있을까 생각해보자. tmp 에는 다음 for문으로 이동하기 위해서 자릿수에 해당하는 해시값을 담아야 한다
    #n2를 tmp로 교체하고 어떻게 다음 항으로 넘길 수 있는가 생각해보자
    #현재 tmp 에는 n2(두번째 자릿 수)가 담겨있는 상황이다. 세번째 자리를 담으면서 동시에 tmp 는 빈 것이어야 하니 교체가 불가능할 것 같다.
    #임시 배열과 자릿수 배열 두가지를 운용해서 임시 배열의 값의 저장이 끝나면 자릿수 배열로 옮김과 동시에 비워내고 이를 다음 자릿수 계산에 활용하면 어떨까? 2차원 배열을 사용하지 않아도 될까?
    
    #N 은 자릿수를 의미한다 그렇다면 아래의 for 문은 4자리일 때는 3회의 연산이 반복되므로 N-1회 반복이 됨을 알 수 있다.
    #for _ in range(N-1):

    #일단 임시배열 tmp 에 1로 시작할 때 둘째자릿수에 해당하는 d[1]을 담았다. 내용은 [0,2]가 된다
    
    #이제 0,2로 시작해서 셋째자릿 수를 구하는 연산을 시작해야 한다 tmp에 담겨있는 자릿수 항목이 필요하나 위에서 tmp 말고 자릿수 배열을 새로 구성하기로 했으므로 복사하고 tmp = [] 선언하도록 하자
    #아래 n은 tmp를 복사할 배열이다
    
    #다음 자리를 구하는 연산이다. 위에서 나타난 반복문과 매우 유사하다. for 문을 사용하여 반복할 수 있을 것 같다. 위에는 첫번째 자릿수, 아래는 두번째 자릿수다.
    #앞으로 셋째, 넷째에 대해서 연산이 더 필요하니, 위에서 쓰려고 했던 for _ in range(N-1)을 사용할 수 있을 것 같다. 감싸도록 해보자
    #N=4일 때, n1~n4로 나타내던 것을 n으로 합쳐보려고 했다. 그렇다면 n1이 아닌 n으로 첫째자리 수도 받아주도록 하자
    n = [num]
    #N 은 자릿수이다. 
    #3차원 for 문이어도 안터질 것이라고 생각했지만 생각보다 너무 많아서 터지는듯하다. memoization을 사용할 수 있는가? 어디에서 적용 가능한가?
    #d[i]를 구하는 과정은 결국 반복되면서 일정한 결과가 나올 것이라 생각한다. 상향식으로 올라가면서 저장이 가능한가??
    #각 과정을 진행하면서? 그러면 어디에서 반복이 되는가를 알아야 한다.
    for _ in range(0,N-1):
        tmp = []
        #tmp 가 비워지지 않고 계속 채워지는 것인가? n이 이상한 것인가?
        for i in n:            
            #현재 tmp 에 넣어주는 것은 첫째자리수가 1이고, n 이 0,2일 때 , i = 0 이면 tmp = [1]이 담기는데, i = 2 일 때, [1,1,3]형태가 돼야 하는데 [1,3]이 돼버려 문제다.
            #n의 형태는 1차원 배열이므로 tmp 는 1차원 배열의 형식은 유지하되 값은 합쳐져야 하므로 반복문과 append를 사용하여 넣어주자. 아마 시간초과는 안날듯 하다. 100 * 10 * 2?정도가 최대?
            #자꾸 tmp 에 1~9가 담긴채로 다음 항으로 안넘어갔는데 아래 for 문에 내가 d[i]를 전달하지 않고 d라는 것을 전달해서 그랬다.
            for j in d[i]:
                tmp.append(j)
                #print(tmp)
        #n 에 다음 자릿수 배열을 받아야 하니 tmp를 받고 tmp는 말했던대로 비워주자
        #n의 갯수는 점점 커져야 정상
        n = tmp
        
        
    #반복문을 다 돌고난 뒤에는 n 에 마지막 자릿수 배열이 담겨있을 것이다.
    #이 값들의 해시 값은 sum 을 통해서 더해주고 return 해주도록 하자. 앞에서 네번째 자릿수의 값의 갯수를 더하고 리턴한것과 같은 행위이다.
    
    #n의 형태가 2차원 배열이다. 그 이유는 무엇인가? 그 이유는 tmp가 2차원 배열의 형태를 띄고 있기 때문이다. 애초에 d의 형태가 arr 이기 때문에 tmp 는 arr로 하지 않도록 해보자

    # for i in n:
        
    #     #d[i]는 arr의 형태이다. 내가 필요한 것은 d[i]가 아니라 i 라는 수가 몇개의 계단수를 가지고 있느냐 이다. 0이면 1, 9면 1, 2~8이면 2이다
    #     #현재 n에는 마지막 자릿수가 담겨있다 그래서 N+1 자리의 값이 추가되는 듯 하다. 위쪽 계산을 N-1까지만 진행하자
    #     #값이 N = 2 일때까지는 제대로 나오지만 그 이상은 나오지 않는다. tmp 와 n 을 저장하고 비우는 과정이 문제인듯 하다.         
    #     
    #     if i ==0 or i == 9:
    #         sum += 1
    #     else:
    #         sum += 2
    #N = 1일때, n 에는 1~9가 저장된다. 끝자리수들의 배열이고 이 길이가 곧 내가 원하는 값이었다
    #print(n)
    print(n)
    return len(n)

for i in range(1,10):
    #sol 에는 첫째자리 수 뿐 아니라, 몇자리 수인지 N을 전달해주어야 한다.
    
    sum += sol(i,N)
print(sum % 1000000000)