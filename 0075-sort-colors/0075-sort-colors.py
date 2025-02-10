class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0,0,0]
        for i in nums:
            res[i]+=1
        ans = []
        k = 0
        for i in range(len(res)):
            while res[i] >0:
                nums[k] = i
                k+=1
                res[i]-=1

            


        