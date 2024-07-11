class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # x = 0
        # while x<n:
        #     if 4**x == n:
        #         return True
        #     else:
        #         if 4**x > n:
        #             return False
        #     x+=1
        while n > 0:
            if n == 1:
                return True
            if n%4 != 0:
                break
            n=n//4
        return False