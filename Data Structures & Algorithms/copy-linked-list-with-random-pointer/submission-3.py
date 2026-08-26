"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        start=Node(head.val)
        curr=start
        ogcurr=head
        map={}
        while ogcurr.next:
            map[ogcurr]=curr
            curr.next=Node(ogcurr.next.val)
            ogcurr=ogcurr.next
            curr=curr.next
        
        map[ogcurr]=curr
        curr.next=None
        curr=start
        ogcurr=head
        
        while ogcurr:
            if ogcurr.random is None:
                curr.random=None
                ogcurr=ogcurr.next
                curr=curr.next
                continue
            ogrnd=ogcurr.random
            rnd=map[ogrnd]
            curr.random=rnd
            ogcurr=ogcurr.next
            curr=curr.next
        
        return start
             
        
        



        