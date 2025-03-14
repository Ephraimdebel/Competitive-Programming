class Solution:
    def countGoodNumbers(self, n: int) -> int:


        def modular(base,exp):
            result = 1
            while exp > 0:
                if exp %2 == 1:
                    result = (result*base) %(10**9+7)
                base = (base*base)%(10**9+7)
                exp//=2
            return result
        no_even = ceil(n/2)
        no_odd = n//2
        even = modular(5,no_even)
        odd = modular(4,no_odd)
        return (even*odd)%(10**9+7)