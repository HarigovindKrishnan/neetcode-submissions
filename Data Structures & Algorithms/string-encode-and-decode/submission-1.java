class Solution {

    public String encode(List<String> strs) {
        String result="";
        for(String s:strs)
        {
            int l=s.length();
            result+=l+"#"+s;
        }
        return result;
    }

    public List<String> decode(String str) {
        int current=0;
        int start=0;
        String l;
        List<String> output=new ArrayList<>();
        while(current<str.length())
        {
            while(str.charAt(current)!='#')
            {
                current++;
            }
            l=str.substring(start,current);
            int n=Integer.parseInt(l);
            String word=str.substring(++current,current+n);
            output.add(word);
            current=current+n+1;
            start=current-1;
        }
        return output;
    }
}
