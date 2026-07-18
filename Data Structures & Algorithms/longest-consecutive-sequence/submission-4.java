class Solution {
    public int longestConsecutive(int[] nums) {
        int count=0,max=0;
        HashMap<Integer,Integer> map=new HashMap<>();

        for(int i=0;i<nums.length;i++)
        {
            map.put(nums[i],1);
        }

        for(int i=0;i<nums.length;i++)
        {
            if(!map.containsKey(nums[i]-1))
            {
                count=0;
                while(map.containsKey(nums[i]+count))
                {
                    count++;
                }
                if(count>max)
                {
                    max=count;
                }
            }
        }

        return max;

    }
}
