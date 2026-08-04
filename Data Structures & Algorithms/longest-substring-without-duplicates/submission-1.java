class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0,r=0,max=0,len=0;
        HashMap<Character,Integer> map=new HashMap<>();
        if(s.length()==1)
        {
            return 1;
        }
        while(r<s.length())
        {
            char c=s.charAt(r);
            if(map.containsKey(c) && map.get(c)>0)
            {
                if(len>max)
                {
                    max=len;
                }

                while(s.charAt(l)!=c)
                {
                    map.put(s.charAt(l),map.get(s.charAt(l))-1);
                    l++;
                    len--;
                }
                l++;
                len--;
                map.put(c,map.get(c)-1);

                
            }
            else
            {
                len++;
                map.put(c,1);
                r++;
            }
        }
        if(len>max)
        {
            max=len;
        }

        return max;
    }
}