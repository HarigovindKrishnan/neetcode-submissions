class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        time=[]
        for i in range(len(position)):
            arr=[]
            arr.append(position[i])
            arr.append(speed[i])
            t=((target-position[i])/speed[i])
            arr.append(t)
            time.append(arr)
        

        time.sort(key=lambda x:x[0], reverse=False)
        stack.append(time[-1][2])
        for i in range(len(position)-2,-1,-1):
            if time[i][2]<=stack[-1]:
                continue
            else:
                stack.append(time[i][2])
        
        return len(stack)


        