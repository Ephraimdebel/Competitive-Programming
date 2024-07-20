class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            if len(nums) == 0:
                return 0
            x =len(nums)
            for i in range(x):
                if val in nums:
                    nums.remove(val)
            result = len(nums)     
            return result
            