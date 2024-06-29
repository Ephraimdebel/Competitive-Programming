class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        x = nums.pop()
        if x not in nums:
            return False
        elif len(nums) > (x):
            return False
        elif len(nums) < x:
            return False
        elif 1 not in nums:
            return False
        y = set(nums)
        if len(y) != len(nums):
            return False

        return True
        
        