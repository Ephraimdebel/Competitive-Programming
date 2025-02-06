class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        res = []
        for key,val in my_dict.items():
            if val ==2:
                res.append(key)
        return res