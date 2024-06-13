class Solution:
    def isPalindrome(self, s: str) -> bool:
        count = 0
        s.strip()
        new = s.lower()
        newstring = ""
        for i in new:
            if i.isalnum():
                
                newstring+=i
        old = len(newstring)        
        m = len(newstring) -1 
        for i in range(m +1):
            

            if newstring[i] is newstring[m-i]:
                
                count+=1
        if count == old:
            return True
        else:
            return False