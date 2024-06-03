class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)
        if(lengthS==lengthT):
            for i in range(lengthS):
                if(s.count(s[i])!=t.count(s[i])):
                    return False
            return True
        