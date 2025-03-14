class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(candies, k, size):
            if size == 0:
                return True
            total = 0
            for candy in candies:
                total += candy // size
                if total >= k:
                    return True
            return False

        if sum(candies) < k:
            return 0

        l, h = 1, max(candies)
        while l < h:
            mid = (l + h + 1) // 2
            if helper(candies, k, mid):
                l = mid
            else:
                h = mid - 1

        return l