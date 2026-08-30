# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt=0
        curr=head
        while curr:
            cnt+=1
            curr=curr.next
        
        limit=cnt//k
        cnt=0
        curr=head
        prev=None
        temp=None
        prevend=ListNode()
        while cnt<limit:
            end=curr
            for i in range(k):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            start=prev
            prevend.next=start
            prevend=end
            end.next=curr
            cnt+=1
            if cnt==1:
                begin=prev
        
        return begin

        