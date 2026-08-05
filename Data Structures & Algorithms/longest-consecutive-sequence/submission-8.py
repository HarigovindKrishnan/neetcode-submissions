class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt=1
        max=0
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1

        r=1
        while r<len(nums):
            if nums[r]==nums[r-1]:
                r+=1
                continue
            if nums[r]==nums[r-1]+1:
                 cnt+=1
                 r+=1
                 continue
            else:
                if cnt>max:
                    max=cnt
                r+=1
                cnt=1
        if cnt>max:
            max=cnt
        return max


            