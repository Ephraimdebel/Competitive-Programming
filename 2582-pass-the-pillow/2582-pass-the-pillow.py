class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        round = time//(n-1)
        ans = 0
        if(round%2==0):
            ans = (time%(n-1))+1
        else:
            ans = n -  (time%(n-1))
        return ans
       