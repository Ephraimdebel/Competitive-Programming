class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l = 0
        r = len(piles) - 2
        piles.sort()
        my_score = []
        
        while l < r:
            my_score.append(piles[r])
            l+=1
            r-=2
        return sum(my_score)
