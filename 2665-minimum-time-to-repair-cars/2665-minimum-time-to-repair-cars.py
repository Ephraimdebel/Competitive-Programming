class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r = 1,ranks[0]*cars*cars

        res = 0
        def count_repaired(t):
            count = 0
            for r in ranks:
                count += int(sqrt(t/r))
            return count
        while l <= r:
            m = (l+r)//2
            repaired = count_repaired(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m+1
        return res