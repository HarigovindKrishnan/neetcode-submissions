class Solution {
    public int maxArea(int[] heights) {
        int l=0,r=heights.length-1;
        int vol=Math.min(heights[l],heights[r])*(r-l);
        while(l<r)
        {
            if(heights[l]<heights[r])
            {
                l++;
                
            }
            else
            {
                r--;
            }

            if(Math.min(heights[l],heights[r])*(r-l)>vol)
            {
                vol=Math.min(heights[l],heights[r])*(r-l);                           
            }
        }

        return vol;       
    }
}
