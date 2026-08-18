class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        stack.append(len(temperatures)-1)
        result=[0]*len(temperatures)
        cnt=0
        for i in range(len(temperatures)-2,-1,-1):
            cnt=0
            while stack and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                result[i]=stack[-1]-i
                stack.append(i)
            else:
                result[i]=0
                stack.append(i)
        
        return result


        