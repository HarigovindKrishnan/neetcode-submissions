class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left=[0]*len(heights)
        right=[0]*len(heights)
        stack=[]
        stack.append(0)

        for i in range(1,len(heights)):
            if heights[i]>heights[stack[-1]]:
                left[i]=stack[-1]+1
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]:
                    stack.pop()
                
                if stack:
                    left[i]=stack[-1]+1
                    stack.append(i)
                else:
                    left[i]=0
                    stack.append(i)

        
        stack=[]
        right[-1]=len(heights)-1
        stack.append(len(heights)-1)
        for i in range(len(heights)-2,-1,-1):
            if heights[i]>heights[stack[-1]]:
                right[i]=stack[-1]-1
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]:
                    stack.pop()
                
                if stack:
                    right[i]=stack[-1]-1
                    stack.append(i)
                else:
                    right[i]=len(heights)-1
                    stack.append(i)
        
        a=0
        ma=0

        for i in range(len(heights)):
            l=right[i]-left[i]+1
            a=l*heights[i]
            ma=max(ma,a)
        
        return ma
                


        