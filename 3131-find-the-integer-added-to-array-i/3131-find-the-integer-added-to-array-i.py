class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        count = 0
        temp = nums1[0]-nums2[0]
        for i in range(len(nums1)):
            result = nums1[i]-nums2[i]
            if temp == result:
                count+=1
        if count ==  len(nums1):
            return (-1)*(temp)

            