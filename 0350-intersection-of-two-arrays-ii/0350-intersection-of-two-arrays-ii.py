class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mylist = [] 
        for i in nums1:
            if i in nums2:
                mylist.append(i)
                nums2.pop(nums2.index(i))
        return mylist
        
            
        