class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        res =[]
        for el in range(len(A),1,-1):
            i = A.index(el)
            res.extend([i+1,el])
            A = A[:i:-1] + A[:i]
        return res