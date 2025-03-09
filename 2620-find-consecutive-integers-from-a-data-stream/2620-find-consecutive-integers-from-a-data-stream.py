class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k 
        self.value = value
        self.deq = deque()
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.deq.append(num)
        else:
            self.deq = deque()
        if len(self.deq) > self.k:
            self.deq.popleft()
        if len(self.deq) == self.k:
            return True
        else:
            return False
        

        



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)