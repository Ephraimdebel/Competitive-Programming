class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        track = [0]*(len(nums) + 1)

        for start,end in requests:
            track[start] += 1
            track[end + 1] -= 1
        for i in range(1,len(track)):
            track[i] += track[i-1]
        track.sort(reverse = True)
        nums.sort(reverse = True)
        
        res = 0
        mod = 10**9 + 7
        for n, count in zip(nums,track):
            res += n*count
        return res%mod
        