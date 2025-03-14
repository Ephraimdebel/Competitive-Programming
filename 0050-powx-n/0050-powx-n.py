class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x,n):
            res = 1
            while n > 0:
                if n%2 == 1:
                    res*=x
                x = x*x
                n//=2
            return res
        ans = 0
        if n >= 0:
            ans = power(x,n)
        else:
            ans = 1/power(x,abs(n))
        return ans
        