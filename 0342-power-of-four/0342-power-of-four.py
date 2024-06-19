class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        while x<n:
            if 4**x == n:
                return True
            else:
                if 4**x > n:
                    return False
            x+=1
        