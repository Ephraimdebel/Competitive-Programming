class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            is_sorted = True
            for j in range(1,len(nums)):
                if nums[j-1] > nums[j]:
                    nums[j-1],nums[j] = nums[j],nums[j-1]
                    is_sorted = False
            if is_sorted:
                break
        


        