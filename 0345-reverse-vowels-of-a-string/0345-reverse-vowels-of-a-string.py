class Solution:
    def reverseVowels(self, s: str) -> str:
        ind = ''
        vow = 'aeiouAEUOI'
        r = ''
        for i in s:
           if i in vow:
            ind = ind + i
        ind = ind[::-1]
        count = 0
        for i in s:
            if i not in vow:
                r = r+ i
            else:
                r = r + ind[count]
                count+=1
        return r

        