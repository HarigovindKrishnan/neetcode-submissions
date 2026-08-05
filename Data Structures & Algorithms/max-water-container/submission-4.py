class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        vol=0
        max=0
        while l<r:
            vol=(r-l)*min(heights[l],heights[r])
            if vol>max:
                max=vol
            
            if heights[l]<heights[r]:
                l+=1;
            else:
                r-=1;
        
        return max

        