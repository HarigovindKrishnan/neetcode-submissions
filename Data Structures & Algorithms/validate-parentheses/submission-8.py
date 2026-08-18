class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)<2:
            return False

        for i in s:
            if i in "{([":
                stack.append(i)
            elif stack:
                x=stack.pop()
                if x=="(" and i==")" or x=="[" and i=="]" or x=="{" and i=="}":
                    continue
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True


        