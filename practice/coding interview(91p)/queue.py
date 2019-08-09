class queue:
    def __init__(self,size):
        self.q_arr = [0]*size
        self.length = 0
        #front = get
        self.front = 0
        #rear = put
        self.rear = 0
        pass
    
    def insert(self, n):
        print(self.rear)
        self.q_arr[self.rear] = n
        self.rear += 1

    def delete(self):
        if self.front == self.rear:
            print("Queue is empty!")
            return -1
        self.ret =  self.q_arr[self.front]        
        self.front += 1
        return self.ret

if __name__ == '__main__':
    q1 = queue(10)
    q1.insert(5)
    q1.insert(3)
    q1.insert(4)
    print(q1.delete())
    print(q1.delete())
    print(q1.delete())