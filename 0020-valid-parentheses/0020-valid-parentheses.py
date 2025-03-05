class Solution:
    def isValid(self, s: str) -> bool:
        parent = {'}':'{',')':'(',']':'['}

        stack = []
        for i in range(len(s)):
            if s[i] == ')' or s[i] ==']' or s[i] == '}':
                if stack:
                    if parent[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack