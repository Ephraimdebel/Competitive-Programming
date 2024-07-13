class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = sorted(s)
        lengthT = sorted(t)
        if(lengthS==lengthT):
            return True
        # for i in range(lengthS):
        #     if(s.count(s[i])!=t.count(s[i])):
        #         return False
        return False
    