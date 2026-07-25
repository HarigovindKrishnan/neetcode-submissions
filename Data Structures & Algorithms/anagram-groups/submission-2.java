class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map=new HashMap<>();
        for(int i=0;i<strs.length;i++)
        {
            String ogword=strs[i];
            char[] c=ogword.toCharArray();
            Arrays.sort(c);
            String keyword=new String(c);
            if(map.containsKey(keyword))
            {
                map.get(keyword).add(ogword);
                continue;
            }
            else
            {
                List<String> list=new ArrayList<>();
                list.add(ogword);
                map.put(keyword,list);
            }
        }

        List<List<String>> result=new ArrayList<>();
        for(String key: map.keySet())
        {
            result.add(map.get(key));
        }
        return result;
        
    }
}
