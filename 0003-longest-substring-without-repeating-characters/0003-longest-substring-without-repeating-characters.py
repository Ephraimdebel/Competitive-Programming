class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        start = 0
        substr = set()
        
        for i in range(len(s)):
            if s[i] not in substr:
                substr.add(s[i])
            else:
                maxlen = max(maxlen, len(substr))
                while s[start] != s[i]:
                    substr.remove(s[start])
                    start += 1
                start += 1
                
        maxlen = max(maxlen, len(substr))
        return maxlen