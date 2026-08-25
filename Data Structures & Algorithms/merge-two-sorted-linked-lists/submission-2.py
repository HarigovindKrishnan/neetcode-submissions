# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        curr1=list1
        curr2=list2
        head=ListNode()
        curr=head
        prev=None
        while curr1 and curr2:
            if prev:
                newnode=ListNode()
                prev.next=newnode
                curr=newnode
                
            if curr1.val<curr2.val:
                curr.val=curr1.val
                curr1=curr1.next
            else:
                curr.val=curr2.val
                curr2=curr2.next
            
            prev=curr
        
        while curr1:
            if prev:
                newnode=ListNode()
                prev.next=newnode
                curr=newnode

            curr.val=curr1.val
            curr1=curr1.next
            
            prev=curr
        
        while curr2:
            if prev:
                newnode=ListNode()
                prev.next=newnode
                curr=newnode

            curr.val=curr2.val
            curr2=curr2.next

            prev=curr
        

        return head



        