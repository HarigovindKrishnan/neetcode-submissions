class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> list=new ArrayList<>();

        for(int i=0;i<nums.length-1;i++)
        {
            for(int j=0;j<nums.length-1-i;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    int temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                }
            }
        }

        System.out.println(Arrays.toString(nums));

        int l=0,r=0;
        for(int i=0;i<nums.length;i++)
        {
            if(i>0 && nums[i]==nums[i-1])
            {
                continue;
            }
            int target=-1*nums[i];
            l=i+1;
            r=nums.length-1;
            while(l<r)
            {
                //if((l>0 && r<nums.length-1) && (nums[l]==nums[l-1] && nums[r]==nums[r+1]) && (nums[l]!=0 && nums[r]!=0))
                //{
                //   l++;
                //    r--;
                //    continue;
                //}
                int sum=nums[l]+nums[r];
                if(sum==target)
                {
                    list.add(Arrays.asList(nums[l],-1*target,nums[r]));
                    l++;
                    while(nums[l]==nums[l-1] && !(nums[l]==0 && nums[r]==0) && l+1<nums.length)
                    {
                        l++;
                    }
                    r--;
                    while(nums[r]==nums[r+1] && !(nums[l]==0 && nums[r]==0) && r>0)
                    {
                        r--;
                    }
                    continue;
                }
                if(sum<target)
                {
                    l++;
                }
                else
                {
                    r--;
                }
            }

        } 
        return list;  
    }
}
