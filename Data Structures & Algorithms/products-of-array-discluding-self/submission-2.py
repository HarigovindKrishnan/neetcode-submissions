class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[0]*len(nums)
        left[0]=1
        left[1]=nums[0]
        for i in range(2,len(nums)):
            left[i]=(left[i-1]*nums[i-1])
        print(left)
        p=1
        for i in range(len(nums)-1,-1,-1):
            left[i]*=p
            p=p*nums[i]
        
        return left