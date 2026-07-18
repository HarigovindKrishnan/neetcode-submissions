class Solution {
    public boolean isPalindrome(String s) { 
        s=s.toLowerCase();
        String str="";
        for(int i=0;i<s.length();i++)
        {
            if((s.charAt(i)>=97 && s.charAt(i)<=122) || (s.charAt(i)>=48 && s.charAt(i)<=57))
            {
                str+=s.charAt(i);
            }
        }

        int l=0,r=str.length()-1;
        System.out.println(str);
        while(l<=r)
        {
            if(str.charAt(l)==str.charAt(r))
            {
                l++;
                r--;
                continue;
            }
            return false;
        }
        return true;

    }
}
