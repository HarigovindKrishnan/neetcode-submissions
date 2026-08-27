class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.limit=capacity
        self.cnt=0
        self.map={}
        self.head=Node()
        self.tail=Node()  
        self.head.next=self.tail
        self.tail.prev=self.head      

    def get(self, key: int) -> int:
        if key in self.map:
            iter=self.head.next
            while iter:
                if iter.key==key:
                    iter.prev.next=iter.next
                    iter.next.prev=iter.prev

                    temp=self.tail.prev
                    temp.next=iter
                    iter.prev=temp

                    iter.next=self.tail
                    self.tail.prev=iter
                    return self.map[key]
                else:
                    iter=iter.next
        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key]=value

            iter=self.head.next
            while iter:
                if iter.key==key:
                    iter.prev.next=iter.next
                    iter.next.prev=iter.prev

                    temp=self.tail.prev
                    temp.next=iter
                    iter.prev=temp
                    iter.next=self.tail
                    self.tail.prev=iter
                    break
                else:
                    iter=iter.next
        

        else:
            if self.cnt==self.limit:
                k=self.head.next.key
                self.map.pop(k)
                self.head.next=self.head.next.next
                self.head.next.prev=self.head

                temp=self.tail.prev
                newnode=Node(key)
                temp.next=newnode
                newnode.prev=temp
                newnode.next=self.tail
                self.tail.prev=newnode
                self.map[key]=value
            
            else:
                newnode=Node(key)
                temp=self.tail.prev
                temp.next=newnode
                newnode.prev=temp
                newnode.next=self.tail
                self.tail.prev=newnode
                self.cnt+=1
                self.map[key]=value

        



        
