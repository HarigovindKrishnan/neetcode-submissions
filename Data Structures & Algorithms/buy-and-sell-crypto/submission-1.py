class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right=[0]*len(prices)
        right[len(prices)-1]=0
        m=0
        p=0
        if len(prices)==1:
            return 0
        for i in range(len(prices)-2,-1,-1):
            right[i]=max(right[i+1],prices[i+1])
        
        for i in range(len(prices)):
            p=right[i]-prices[i]
            if p>m:
                m=p
        
        return m


            