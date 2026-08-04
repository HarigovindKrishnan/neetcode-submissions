class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower()
        t=t.lower()
        m1=[0]*26
        m2=[0]*26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            m1[ord(s[i])-ord('a')]+=1
            m2[ord(t[i])-ord('a')]+=1

        if m1==m2:
            return True
        else:
            return False
