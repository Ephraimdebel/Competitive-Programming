class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                r =int(stack.pop())
                ans = int(stack[-1]) + r
                stack.pop()
                stack.append(ans)
            elif i == "/":
                r =int(stack.pop())
                ans = int(stack[-1]) / r
                stack.pop()
                stack.append(ans)
            elif i == "-":
                r =int(stack.pop())
                ans = int(stack[-1]) - r
                stack.pop()
                stack.append(ans)

            elif i == "*":
                r = int(stack.pop())
                ans = (int(stack[-1])) * (int(r))
                stack.pop()
                stack.append(ans)
            else:
                stack.append(i)
        res = int(stack[-1])
        return res