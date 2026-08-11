class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.min=0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack)==0 or val<self.minstack[-1]:
            self.min=val
            self.minstack.append(self.min)
        else:
            self.minstack.append(self.minstack[-1])
                

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
