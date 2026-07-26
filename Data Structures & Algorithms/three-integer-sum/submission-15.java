class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int l=1,r=nums.length-1;
        List<List<Integer>> result=new ArrayList<>();
        for(int i=0;i<nums.length-2;i++)
        {
            if(i>0 && nums[i]==nums[i-1])
            {
                continue;
            }
            l=i+1;
            r=nums.length-1;
            while(l<r)
            {
                int sum=nums[l]+nums[r];
                if(sum==-(nums[i]))
                {
                    List<Integer> list=new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[l]);
                    list.add(nums[r]);
                    result.add(list);

                    while(l<r && nums[l]==nums[l+1])
                    {
                        l++;
                    }
                    l++;

                    while(r>l && nums[r]==nums[r-1])
                    {
                        r--;
                    }
                    r--;
                    continue;
                }
                if(sum<-(nums[i]))
                {
                    while(l<r && nums[l]==nums[l+1])
                    {
                        l++;
                    }
                    l++;
                }
                else
                {
                    while(r>l && nums[r]==nums[r-1])
                    {
                        r--;
                    }
                    r--;
                }

            }
            
        }

        return result;
    }
}
