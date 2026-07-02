class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int srch=target-nums[i];
            if(map.containsKey(srch))
            {
                return new int[]{map.get(srch),i};
            }
            map.put(nums[i],i);
        }
        return null;
    }
}
