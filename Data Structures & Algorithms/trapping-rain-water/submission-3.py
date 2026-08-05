class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)
        right=[0]*len(height)
        left[0]=0
        right[len(height)-1]=0
        sum=0
        for i in range(1,len(height)):
            left[i]=max(left[i-1],height[i-1])
        
        for i in range(len(height)-2,-1,-1):
            right[i]=max(right[i+1],height[i+1])
        
        vol=0
        for i in range(len(height)):
            vol=min(left[i],right[i])-height[i]
            if vol>0:
                sum+=vol
        
        return sum