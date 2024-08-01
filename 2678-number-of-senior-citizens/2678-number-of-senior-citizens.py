class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for p in details:
            if int(p[-4]+p[-3])>=61:
                count+=1
        return count


        