class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_i = None
        max_i = None
        first_bad = -1
        count = 0

        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                first_bad = i
            if nums[i] == minK:
                min_i = i
            if nums[i] == maxK:
                max_i = i
            
            if max_i != None and min_i != None:
                last = min(max_i,min_i)
                if last > first_bad:
                    count += last - first_bad
        return count