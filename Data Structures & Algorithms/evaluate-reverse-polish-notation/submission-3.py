class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        num=0
        for i in  tokens:
            if i not in "+-/*":
                stack.append(int(i))
            else:
                if i=="+":
                    a=stack.pop()
                    b=stack.pop()
                    num=a+b
                    stack.append(num)
                elif i=="-":
                    a=stack.pop()
                    b=stack.pop()
                    num=b-a
                    stack.append(num)
                elif i=="*":
                    a=stack.pop()
                    b=stack.pop()
                    num=a*b
                    stack.append(num)
                else:
                    a=stack.pop()
                    b=stack.pop()
                    num=int(b/a)
                    stack.append(num)
        
        return stack[-1]
        