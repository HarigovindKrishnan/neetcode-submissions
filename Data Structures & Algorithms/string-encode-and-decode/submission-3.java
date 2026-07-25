class Solution {

    public String encode(List<String> strs) {
         String result="";
         int length=0;
         for(String s:strs)
         {
            length=s.length();
            result+=length+"#"+s;
         }

         return result;
    }

    public List<String> decode(String str) {
        List<String> list=new ArrayList<>();
        int s=0,e=0;
        while(e<str.length())
        {
            while(str.charAt(e)!='#')
            {
                e++;
            }
            
            String length=str.substring(s,e);
            int l=Integer.parseInt(length);
            String word=str.substring(e+1,e+l+1);
            list.add(word);
            s=e+l+1;
            e=s;
        }

        return list;
    }
}
