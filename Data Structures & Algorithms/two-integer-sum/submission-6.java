class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int n=target-nums[i];
            if(map.containsKey(n))
            {
                int[] arr=new int[2];
                arr[0]=map.get(n);
                arr[1]=i;
                return arr;
            }
            map.put(nums[i],i);
        }        
        return null;
    }
}
