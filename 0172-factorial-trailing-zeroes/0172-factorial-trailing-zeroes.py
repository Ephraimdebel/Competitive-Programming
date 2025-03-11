class Solution:
    def trailingZeroes(self, n: int) -> int:

        def factorial(n):
            if n < 5:
                return 0
            ans = n//5 + factorial(n//5)
            return ans
        return factorial(n)