class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map=new HashMap<>();
        for(int i=0;i<strs.length;i++)
        {
            char[] word=strs[i].toCharArray();
            int[] count=new int[26];
            for(int j=0;j<word.length;j++)
            {
                count[(word[j])-'a']++;
            }
            String scount=Arrays.toString(count);
            if(map.containsKey(scount))
            {
                String ogword=new String(word);
                map.get(scount).add(ogword);
            }
            else
            {
                String ogword=new String(word);
                map.put(scount,new ArrayList<>());
                map.get(scount).add(ogword);
            }
        }
        return new ArrayList<>(map.values());
    }
}
