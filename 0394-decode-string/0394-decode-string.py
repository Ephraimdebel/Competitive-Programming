class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                temp = []
                n =""
                while (stack[-1]) != '[':
                    temp.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isnumeric():
                    n = stack.pop() + n
                
                n = int(n)
                res = (n*temp)[::-1]
                stack.append("".join(res))
            else:
                stack.append(i)
    
        return "".join(stack)