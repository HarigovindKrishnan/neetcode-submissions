class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t=0
        b=len(matrix)-1
        flag=0
        while t<=b:
            c=(t+b)//2
            if target in matrix[c]:
                print("hi")
                nums=matrix[c]
                print(nums)
                flag=1
                break
            
            if target>matrix[c][0]:
                t=c+1
                continue
            
            b=c-1
        
        if flag==0:
            return False
        
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return True
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1
        
        return False
                
