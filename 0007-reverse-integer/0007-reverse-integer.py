class Solution:
    def reverse(self, x: int) -> int:
        # Check if the number is within the range of a 32-bit signed integer
        if x > 2147483647 or x < -2147483648:
            return 0

        else:

            s = str(x)
            
            new = []
            for i in s:
                
                new.append(i)
            length= len(new)
            newlist = []
            for i in range(length):
                newlist.append(new.pop())
            if x<0:
                newlist.pop()
                result = -1*int("".join(newlist))
            else:
                result = int("".join(newlist))
            if result > 2147483647 or result < -2147483648:
                return 0
            else:

                return result
