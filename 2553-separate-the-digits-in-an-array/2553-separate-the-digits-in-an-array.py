class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            for i in (str(i)):
                    res.append(int(i))
        return res
                
        