class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minimum=nums[0]
        while l<=r:
            m=(l+r)//2
            if nums[l]<=nums[m]:
                minimum=min(nums[l],minimum)
                l=m+1
                continue
            
            else:
                minimum=min(nums[m],minimum)
                r=m-1
                continue
        
        return minimum
         
        