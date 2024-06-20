class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        case = True
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return case
