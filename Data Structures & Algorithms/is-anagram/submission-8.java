class Solution {
    public boolean isAnagram(String s, String t) {
        int n1=s.length();
        int n2=t.length();

        if(n1!=n2)
        {
            return false;
        }

        s=s.toLowerCase();
        t=t.toLowerCase();

        int[] arr=new int[26];
        int arr2[]=new int[26];
        for(int i=0;i<n1;i++)
        {
            arr[s.charAt(i)-'a']++;
            arr[t.charAt(i)-'a']--;
        }

        if(Arrays.equals(arr, arr2))
        {
            return true;
        }
        return false;

    }
}
