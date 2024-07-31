class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        presum = 0
        mi = float("inf")
        for i in range(len(nums)):
            presum+=nums[i]
            mi = min(mi,presum)
        if mi <= 0:
            return -1*(mi-1)
        if mi>=1:
            return 1
        