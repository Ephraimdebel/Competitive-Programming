class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        l = 0
        r = len(p)
        start = s[l:r]
        compare = defaultdict(int)
        res = []

        for i in start:
            compare[i]+=1
        while r < len(s):

            if compare == count_p:
                res.append(l)
            compare[s[r]]+=1
            compare[s[l]]-=1

            if compare[s[l]] == 0:
                del compare[s[l]]

            r+=1
            l+=1
        if compare == count_p:
            res.append(l)
        return res