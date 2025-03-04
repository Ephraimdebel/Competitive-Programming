class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        s.sort()
        j = len(s)-2
        for i in range(len(s)//2):
            s[i] , s[j-i] = s[j-i],s[i]
        return "".join(s)