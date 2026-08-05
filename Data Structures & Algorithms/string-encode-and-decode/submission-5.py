class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for i in strs:
            n=len(i)
            a+=str(n)+"#"+i

        return a     

    def decode(self, s: str) -> List[str]:
        l=0
        r=0
        result=[]
        word=""
        while r<len(s):
            while(s[r]!='#'):
                r+=1
            
            n=int(s[l:r])
            word=s[r+1:r+n+1]
            result.append(word)
            l=r+1+n
            r=l
        
        return result

