class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return ['0']
            use = helper(n-1)
            stack = ['1']

            for i in use[::-1]:
                if i == '0':
                    stack.append('1')
                else:
                    stack.append('0')
            return use+stack
        ans = helper(n)
        return ans[k-1]