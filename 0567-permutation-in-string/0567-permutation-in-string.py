class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        count_s1 = Counter(s1)
        pre_s = defaultdict(int)
        l = 0
        if len(s1) > len(s2):
            return False
        for i in range(window_size):
            pre_s[s2[i]]+=1

        if pre_s == count_s1:
            return True

        for r in range(window_size,len(s2)):
            
            pre_s[s2[l]]-=1
            pre_s[s2[r]]+=1

            if pre_s[s2[l]] == 0:
                del pre_s[s2[l]]
            if pre_s == count_s1:
                return True
            l+=1
        

        return False