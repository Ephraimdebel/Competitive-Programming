class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,L,M,R):
            left,right = arr[L:M+1],arr[M+1:R+1]
            i = L
            j = 0
            k = 0
            
            while j < len(left) and k <len(right):
                #merge from the left
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                #merging from the right arr
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            while k <len(right):
                arr[i] = right[k]
                k+=1
                i+=1
        def divide(arr, l, r):
            if l == r:
                return arr
            
            m = (l+r)//2
            divide(arr,l,m)
            divide(arr,m+1,r)

            merge(arr,l,m,r)

            return arr
        return divide(nums,0,len(nums)-1)
