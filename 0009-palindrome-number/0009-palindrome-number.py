class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = ""
        n = 0
        original = len(str(x))
        old = x
        
        while n < original:
            y = x%10
            new += str(y)

            n+=1
            x = x//10
            
        if old == int(new):
            return True
        else:
            return False


        