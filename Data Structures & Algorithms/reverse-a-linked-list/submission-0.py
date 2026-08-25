# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=curr=temp=None
        curr=head
        if curr is None:
            return None
        while curr.next is not None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        head=curr
        head.next=prev
        return head


        
        