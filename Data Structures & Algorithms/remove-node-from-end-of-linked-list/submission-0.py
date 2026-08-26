# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        prev=None
        cnt=0
        while curr:
            cnt+=1
            curr=curr.next
        
        target=cnt-n
        if target==0:
            head=head.next
        else:
            cnt=0
            curr=head
            while curr:
                if cnt==target:
                    prev.next=curr.next
                    break
                cnt+=1
                prev=curr
                curr=curr.next
        
        return head

        

        