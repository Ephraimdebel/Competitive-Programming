class Solution:
    def coloredCells(self, n: int) -> int:
    
        m = 0
        pre = 1
        for i in range(n):
            pre+=m
            m+=4
        return pre
        
