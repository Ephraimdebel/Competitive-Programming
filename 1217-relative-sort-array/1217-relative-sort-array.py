class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for i in arr2:
            while count[i] > 0:
                res.append(i)
                count[i] -= 1
        remain = []
        for i in arr1:
            if i not in arr2:
                remain.append(i)
        remain.sort()
        res.extend(remain)
        return res
