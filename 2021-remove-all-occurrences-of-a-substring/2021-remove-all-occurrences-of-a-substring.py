class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= len(part):
                r = -1* len(part) 
                temp = "".join(stack[r:])
                
                if temp == part:

                    l = len(stack) - len(part)
                    stack = stack[:l]
            
        return "".join(stack)