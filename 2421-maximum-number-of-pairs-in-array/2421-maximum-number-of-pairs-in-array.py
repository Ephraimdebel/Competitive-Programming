class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count= 0
        remain = 0
        my_dict = Counter(nums)
        for i in my_dict.values():
            mod = i%2
            qou = i//2
            count+=qou
            remain+=mod
        return [count,remain]