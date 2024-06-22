class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = {}  
        for i in s:
            n[i] = n.get(i, 0) + 1    
        for j, i in enumerate(s):
            if n[i] == 1:
                return j

        return -1  
            