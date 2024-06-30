class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sums = 0
        l = len(nums)
        nums.append(0)
        for i in range (len(nums)):
            if nums[i] == nums[i+1]-1:
                sums += nums[i]
            else:
                sums+=nums[i]
                break
        while True:
            if sums not in nums:
                return sums
            sums+=1
        