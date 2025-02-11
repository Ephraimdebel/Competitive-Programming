class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_small = defaultdict(int)
        new_sorted = sorted(nums)

        for i in range(len(new_sorted)):
            if new_sorted[i] not in count_small:
                count_small[new_sorted[i]] = i
        
        res =[]
        for i in nums:
            res.append(count_small[i])
        return res

