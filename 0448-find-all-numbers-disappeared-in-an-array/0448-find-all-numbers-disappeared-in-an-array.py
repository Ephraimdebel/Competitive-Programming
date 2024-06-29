class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        maximum = max(nums_set)
        length = len(nums)
        maxim = max(maximum, length)
        missing_elements = []
        for i in range(1, maxim+1):
            if i not in nums_set:
                missing_elements.append(i)
        return missing_elements  
            