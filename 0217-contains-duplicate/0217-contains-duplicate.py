class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        nums.sort()
        n=len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False