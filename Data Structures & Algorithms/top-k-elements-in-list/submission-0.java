class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                map.put(nums[i],map.get(nums[i])+1);
            }
            else
            {
                map.put(nums[i],1);
            }
        }

        ArrayList<Integer>[] freq=new ArrayList[nums.length];
        for(int key: map.keySet())
        {
            int val=map.get(key);
            if(freq[val-1]==null)
            {
                freq[val-1]=new ArrayList<>();
            }
            freq[val-1].add(key);
        }

        int[] result=new int[k];
        int count=0;
        for(int i=nums.length-1;i>=0 && count<k;i--)
        {
            if(freq[i]!=null)
            {
                for(int j: freq[i])
                {
                    result[count++]=j;
                    if(count==k)
                    {
                        break;
                    }
                }        
            }
        }

        return result;
    }
}
