class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # sum = 0
        # org = x
        # while x!=0:
        #     y = x%10
        #     sum+=y
        #     x//=10
        # if org%sum==0:
        #     return sum
        # else:
        #     return -1
        sum=0
        for i in str(x):
            sum += int(i)
        if x%sum==0:
            return sum
        else: 
            return -1

        