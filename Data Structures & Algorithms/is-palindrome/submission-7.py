class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=""
        for i in s:
            x=ord(i)
            if (x>64 and x<91) or (x>96 and x<123) or (x>47 and x<58):
                st+=i
        
        print(st)
        l=0
        r=len(st)-1
        while l<r:
            if st[l]==st[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True

        