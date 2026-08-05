class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        l=0
        r=0
        cnt=0
        max=0
        while r<len(s):
            if s[r] in freq and freq[s[r]]==1:
                if cnt>max:
                    max=cnt
                
                while s[l]!=s[r]:
                    freq[s[l]]=0
                    l+=1
                    cnt-=1
                    
                l+=1
                cnt-=1
                freq[s[r]]=0

            else:
                freq[s[r]]=1
                cnt+=1
                r+=1
            
        if cnt>max:
            max=cnt
        
        return max
            
        