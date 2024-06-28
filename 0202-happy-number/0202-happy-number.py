class Solution:
    def isHappy(self, n: int) -> bool:
        while n>6:
            x = str(n)
            sum = 0
            for i in x:
                sum += (int(i))**2
            n = sum
        if n == 1:
            return True
        return False



        