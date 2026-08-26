class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited=[]
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if fast==slow:
                break 

        slow=nums[0]
        while True:
            if slow==fast:
                return slow
            else:
                slow=nums[slow]
                fast=nums[fast]


        return slow
        