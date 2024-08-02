class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon={
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
            }
        for j in text:
            if j in balloon:
                balloon[j] += 1 
        balloon['l'] //= 2
        balloon['o'] //= 2
        return min(balloon.values())
            

        