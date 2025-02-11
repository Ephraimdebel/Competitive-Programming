class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations) 
        for i in range(N):
            if citations[i] >= N -i:
                print(citations)
                return N-i
 
        return 0