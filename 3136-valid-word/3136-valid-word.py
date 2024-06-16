class Solution:
    def isValid(self, word: str) -> bool:
        vowel = "aeiouAEIOU"
        newv = 0
        count = 0
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        for k in word:
            if k in vowel:
                newv+=1
        if newv == 0:
            return False
        for w in word:
            if w not in vowel and w.isalpha():
                count+=1
        if count == 0:
            return False
        return True
            
            
                
                
        