class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(arr,left,right):
            if left == right:
                return arr[left]
            score_left = arr[left] - helper(arr,left+1,right)
            score_right = arr[right] - helper(arr,left,right-1)
            return max(score_left,score_right)
        res = helper(nums,0,len(nums)-1)
        return res >= 0