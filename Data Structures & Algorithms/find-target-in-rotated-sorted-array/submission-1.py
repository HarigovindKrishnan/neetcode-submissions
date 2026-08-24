class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            if nums[m]>=nums[l]:
                if target<nums[m] and target>=nums[l]:
                    r=m-1
                    continue
                else:
                    l=m+1
                    continue
            else:
                if target>nums[m] and target<nums[l]:
                    l=m+1
                else:
                    r=m-1
        
        return -1


