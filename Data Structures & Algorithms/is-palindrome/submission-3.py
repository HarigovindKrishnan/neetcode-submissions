class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=""
        for i in s:
            if i.isalnum():
                st+=i

        if st=="".join(reversed(st)):
            return True
        else:
            return False
        