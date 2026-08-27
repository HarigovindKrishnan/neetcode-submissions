class Node:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.limit=capacity
        self.cnt=0
        self.head=Node()
        self.tail=Node()
        self.map={}

        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if key in self.map:
            node=self.map[key]
            node.prev.next=node.next
            node.next.prev=node.prev

            temp=self.tail.prev
            temp.next=node
            node.prev=temp

            node.next=self.tail
            self.tail.prev=node
            return node.value
        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node=self.map[key]
            node.value=value
            node.prev.next=node.next
            node.next.prev=node.prev

            temp=self.tail.prev
            temp.next=node
            node.prev=temp

            node.next=self.tail
            self.tail.prev=node

        else:
            if self.cnt==self.limit:
                k=self.head.next.key
                self.head.next=self.head.next.next
                self.head.next.prev=self.head

                self.map.pop(k)
                temp=self.tail.prev
                newnode=Node(key,value)
                temp.next=newnode
                newnode.prev=temp

                newnode.next=self.tail
                self.tail.prev=newnode

                self.map[newnode.key]=newnode
            else:
                self.cnt+=1
                temp=self.tail.prev
                newnode=Node(key,value)
                temp.next=newnode
                newnode.prev=temp

                newnode.next=self.tail
                self.tail.prev=newnode
                self.map[newnode.key]=newnode

        
