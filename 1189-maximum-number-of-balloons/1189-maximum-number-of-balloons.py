class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = float("inf")
        word = "balloon"
        my_counter = Counter(char for char in text if char in word)
        for i in word:
            if i not in my_counter:
                return 0
        for k,v in my_counter.items():   
            if k in ["l","o"]:
                ans = v//2
            else:
                ans = v
            res = min(ans,res)
        return res
            

        