class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='{' or i=='[' or i=='(':
                stack.append(i)
            
            else:
                if len(stack)==0:
                    return False
                
                x=stack.pop()
                if x=='{' and i=='}' or x=='(' and i==')' or x=='[' and i==']':
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        