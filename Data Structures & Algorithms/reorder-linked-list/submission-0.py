# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow

        curr=second
        prev=None
        temp=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        a=head
        b=prev

        while a!=slow and b:
            temp1=a.next
            temp2=b.next
            a.next=b
            b.next=temp1
            a=temp1
            b=temp2

        if a.next==a:
            a.next=None
        
        
        curr=head
        ans=[]
        while curr:
            ans.append(curr.val)
            curr=curr.next
        
        print(ans) 
            




        


        