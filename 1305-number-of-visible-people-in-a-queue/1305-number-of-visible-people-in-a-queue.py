class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0]*len(heights)
        d = 0
        for i in range(len(heights)):
            t = 1
            while stack and heights[stack[-1]] <= heights[i]:
                res[stack.pop()] += 1
                t+=1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res