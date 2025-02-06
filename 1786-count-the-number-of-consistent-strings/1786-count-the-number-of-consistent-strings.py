class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            flag = True
            res = set(i)
            for i in res:
                if i not in allowed:
                    flag = False
            count += (1 if flag else 0)
        return count


        