class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m=dict()
        for i in range(len(nums)):
            s=target-nums[i]
            if m.get(s) != None:
                return [m[s],i]
            else:
                m[nums[i]]=i
    
        return []
        

