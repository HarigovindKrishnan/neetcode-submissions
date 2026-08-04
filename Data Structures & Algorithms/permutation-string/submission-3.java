class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] arr=new int[26];
        int[] temp=new int[26];

        if(s1.length()>s2.length())
        {
            return false;
        }

        for(char c: s1.toCharArray())
        {
            arr[c-'a']++;
        }

        for(int i=0;i<s1.length();i++)
        {
            temp[s2.charAt(i)-'a']++;            
        }

        for(int i=s1.length();i<s2.length();i++)
        {
            if(Arrays.equals(arr,temp))
            {
                return true;
            }
            temp[s2.charAt(i)-'a']++;
            temp[s2.charAt(i-s1.length())-'a']--;
        }

        if(Arrays.equals(arr,temp))
        {
            return true;
        }

        return false;
    }
}
