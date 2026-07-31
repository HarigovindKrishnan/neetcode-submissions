class Solution {
    public int maxProfit(int[] prices) {
        int[] right=new int[prices.length];
        if(prices.length==1)
        {
            return 0;
        }
        right[prices.length-1]=prices[prices.length-1];
        for(int i=prices.length-2;i>=0;i--)
        {
            right[i]=Math.max(right[i+1],prices[i+1]);
        }

        int max=0;
        for(int i=0;i<prices.length;i++)
        {
            if(right[i]-prices[i]>max)
            {
                max=right[i]-prices[i];
            }
        }

        return max;

    }
}
