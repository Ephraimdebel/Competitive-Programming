class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))  # Remove duplicates from the list
        
        max_length = 1
        current_length = 1
        
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)