class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            s=target-nums[i]
            if s in map:
                return [map[s],i]
            else:
                map[nums[i]]=i
        
        return []
        