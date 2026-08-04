class Solution {
    public int characterReplacement(String s, int k) {
        int[] arr=new int[26];
        int l=0,r=0;
        int max=0,mf=0;
        for(r=0;r<s.length();r++)
        {
            char c=s.charAt(r);
            arr[c-'A']++;
            mf=Math.max(mf,arr[c-'A']);

            if((r-l+1)-mf>k)
            {
                arr[s.charAt(l)-'A']--;
                l++;
            }
            max=Math.max((r-l)+1,max);
        }

        return max;
    }
}
