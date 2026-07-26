class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                map.put(nums[i],map.get(nums[i])+1);
                continue;
            }
            map.put(nums[i],1);
        }

        List<Integer> list=new ArrayList<>();
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]-1))
            {
                continue;
            }
            list.add(nums[i]);
        }

        int cnt=0,max=0;
        for(int n:list)
        {
            cnt=0;
            int temp=n;
            while(map.containsKey(temp))
            {
                cnt++;
                temp++;
            }
            if(cnt>max)
            {
                max=cnt;
            }
        }

        return max;
        
    }
}
