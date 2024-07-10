class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = 0
        for i in logs:
            if i[0].isalnum():
                curr+=1
            elif i[0] == ".":
                if i[1] == "." and curr!=0:
                    curr-=1
                else:
                    pass      
        return curr
        