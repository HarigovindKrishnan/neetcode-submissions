class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for i in range(len(position)):
            x=[]
            x.append(position[i])
            x.append(speed[i])
            x.append((target-position[i])/speed[i])
            time.append(x)
        
        time.sort(key=lambda x:x[0], reverse=False)
        stack=[]
        stack.append(time[-1][2])
        cnt=1
        for i in range(len(position)-2,-1,-1):
            if time[i][2]<=stack[-1]:
                continue
            else:
                stack.append(time[i][2])
                cnt+=1
        
        return cnt



