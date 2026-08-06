class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        map1={}
        for i in t:
            map1[i]=map1.setdefault(i,0)+1

        need=len(map1)
        have=0
        map2={}
        length=0
        min=len(s)
        result=""

        for r in range(len(s)):
            map2[s[r]]=map2.setdefault(s[r],0)+1
            if s[r] in map1:
                if map2[s[r]]==map1[s[r]]:
                    have+=1
            
            while have==need:
                length=r-l+1
                if length<=min:
                    min=length
                    result=s[l:r+1]
                
                map2[s[l]]-=1
                if s[l] in map1:
                    if map2[s[l]]<map1[s[l]]:
                        have-=1
                    l+=1
                
                else:
                    l+=1
        print(min)
        return result




            
