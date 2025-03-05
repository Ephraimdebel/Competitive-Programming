class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.d = deque()
    def consec(self, num: int) -> bool:
        
            
        if num == self.value:
            self.d.append(num)
        else:
            self.d = deque()
        return len(self.d) >= self.k



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)