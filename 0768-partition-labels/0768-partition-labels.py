class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}
        k,j = 0,0
        ans = []
        for i,c in enumerate(s):
            j = max(j,last[c])
            if i == j:
                ans.append(i-k+1)
                k = i+1
        return ans