class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre_sum = sum(nums[:k])
        max_ = pre_sum
        for l in range(len(nums)-k):
            pre_sum += nums[l+k] - nums[l]  
            max_ = max(pre_sum,max_)
        return max_/k