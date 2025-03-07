class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = deque()
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.count<self.k:
            self.queue.appendleft(value)
            self.count+=1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.count<self.k:
            self.queue.append(value)
            self.count+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.queue)==0:
            return False
        self.queue.popleft()
        self.count-=1
        return True

    def deleteLast(self) -> bool:
        if len(self.queue)==0:
            return False
        self.queue.pop()
        self.count-=1
        return True

    def getFront(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.k == self.count:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()