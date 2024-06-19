class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        org = x
        while x!=0:
            y = x%10
            sum+=y
            x//=10
        if org%sum==0:
            return sum
        else:
            return -1

        