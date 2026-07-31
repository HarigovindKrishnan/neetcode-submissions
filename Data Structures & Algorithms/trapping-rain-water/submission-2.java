class Solution {
    public int trap(int[] heights) {
        int sum=0;
        int[] left=new int[heights.length];
        int[] right=new int[heights.length];
        int vol=0;
        if(heights.length==1)
        {
            return 0;
        }
        right[heights.length-2]=heights[heights.length-1];
        left[1]=heights[0];
        for(int i=2;i<heights.length-1;i++)
        {
            left[i]=Math.max(left[i-1],heights[i-1]);
        }

        for(int i=heights.length-2;i>=1;i--)
        {
            right[i]=Math.max(right[i+1],heights[i+1]);
        }

        for(int i=1;i<heights.length-1;i++)
        {
            vol=Math.min(left[i],right[i])-heights[i];
            if(vol>0)
            {
                sum+=vol;
            }
        }

        return sum;
    }
}
