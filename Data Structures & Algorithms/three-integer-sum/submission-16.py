class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            print(target)
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[l]+nums[r]
                if sum==target:
                    result.append([nums[i],nums[l],nums[r]])
                    
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    l+=1

                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                
                elif sum<target:
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    l+=1

                else:
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
            
        return result
            




