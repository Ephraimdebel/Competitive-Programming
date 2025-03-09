class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        count = 0
        l = 0
        N =len(colors)

        for r in range(1,N + k - 1):
            if colors[r%N] == colors[(r-1)%N]:
                l = r
            if r-l+1 > k:
                l+=1
            if r - l + 1 == k:
                count+=1
            
        return count