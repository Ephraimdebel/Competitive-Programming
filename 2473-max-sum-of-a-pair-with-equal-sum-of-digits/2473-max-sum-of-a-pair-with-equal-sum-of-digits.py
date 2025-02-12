from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_ = -1
        same_dig = defaultdict(list)
        
        def digit_sum(x):
            res = 0
            while x > 0:
                res += x % 10
                x //= 10
            return res
        
        for num in nums:
            dig = digit_sum(num)
            same_dig[dig].append(num)
        
        for key in same_dig:
            if len(same_dig[key]) >= 2:
                same_dig[key].sort(reverse=True)
                max_ = max(max_, same_dig[key][0] + same_dig[key][1])
        
        return max_