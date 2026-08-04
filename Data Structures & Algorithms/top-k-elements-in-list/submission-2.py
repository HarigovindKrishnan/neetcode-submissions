class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=dict()
        for i in nums:
            map[i]=map.setdefault(i,0)+1
        
        freq=[[] for _ in range(len(nums))]
        for i in map:
            freq[map[i]-1].append(i)
        
        cnt=0
        result=[]
        for i in range(len(nums)-1,-1,-1):
            for j in freq[i]:
                result.append(j)
                cnt+=1
                if(cnt==k):
                    return result
        
        return []
                


