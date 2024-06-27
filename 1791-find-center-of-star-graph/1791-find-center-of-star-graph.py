class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mydict = {}
        for i in range(len(edges)):
            mydict[i] = edges[i]
        prob1 = edges[0][0]
        prob2 = edges[0][1]
        for values in mydict.values():
            if prob1 not in values:
                return prob2
        return prob1 
            

        