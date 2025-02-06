class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pro = nums[i]*nums[j]
                product[pro]+=1
        count = 0
        for val in product.values():
            if val > 1:
                count += (val*(val-1))*4
        return count