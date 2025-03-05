class RecentCounter:

    def __init__(self):
        self.start = 0
        self.ls = []

    def ping(self, t: int) -> int:
        self.ls.append(t)
        while ( t-self.ls[self.start]) > 3000:
            self.start += 1
        return len(self.ls) - self.start



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)