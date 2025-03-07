class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = [0]

        for i in s:
            if i == '(':
                stack.append(0)
            else:
                a = stack.pop()
                if a == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*a
        return stack[0]