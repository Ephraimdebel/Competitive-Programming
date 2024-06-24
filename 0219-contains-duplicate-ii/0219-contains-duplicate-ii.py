class Solution:
    def containsNearbyDuplicate(self, nums, k):
        Dict = {}  

        for i, num in enumerate(nums):
            if num in Dict and i - Dict[num] <= k:
                return True  
            Dict[num] = i

        return False

            