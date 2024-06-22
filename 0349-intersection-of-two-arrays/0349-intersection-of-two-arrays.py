class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myDict = {}
        myList = []
        for i in nums1:
            if i in nums2:
                if i not in myDict:
                    myDict[i] = 1
                else:
                    myDict[i]+=1
        for key,value in myDict.items():
            myList.append(key)
        return myList
        