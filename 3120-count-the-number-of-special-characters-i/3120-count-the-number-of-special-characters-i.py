class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        newString = ""
        count=0
        for i in word:
            if i not in newString:
                if i.isupper():
                    res =  ord(i)+32
                else:
                    res = ord(i)-32
                if chr(res) in word:
                    count +=1
                    newString+=i
                    newString+=chr(res)
        return count
            