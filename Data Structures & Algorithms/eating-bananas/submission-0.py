class Solution:
    def time(self,k:int,piles: List[int])->k:
            sum=0
            for i in piles:
                sum+=math.ceil(i/k)
            
            return sum
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        minimum=r

        while(l<=r):
            m=(l+r)//2
            t=self.time(m,piles)
            if t<=h:
                minimum=m
                r=m-1
            else:
                l=m+1
        
        return minimum




        
        
