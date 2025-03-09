class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k 
        self.value = value
        self.deq = deque()
        self.count = 0
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.deq.append(num)
            self.count+=1
        else:
            self.count = 0
        if self.count > self.k:
            t = self.deq.popleft()
            if t == self.value:
                self.count-=1
        if self.count == self.k:
            return True
        else:
            return False
        

        



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)