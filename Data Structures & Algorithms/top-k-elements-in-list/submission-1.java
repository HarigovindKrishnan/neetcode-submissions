class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        List<Integer>[] list=new ArrayList[nums.length];
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                map.put(nums[i],map.get(nums[i])+1);
                continue;
            }
            map.put(nums[i],1);
        }

        for(int i=0;i<nums.length;i++)
        {
            list[i]=new ArrayList<>();
        }

        for(int key:map.keySet())
        {
            list[map.get(key)-1].add(key);
        }

        int cnt=0;
        int[] result=new int[k];
        for(int i=nums.length-1;i>=0 && cnt<k;i--)
        {
            if(list[i].isEmpty())
            {
                continue;
            }

            for(int element:list[i])
            {
                if(cnt>k)
                {
                    break;
                }
                result[cnt]=element;
                cnt++;
            }

        }

        return result;
    }
}
