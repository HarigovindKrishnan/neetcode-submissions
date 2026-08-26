# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        curr1=l1
        curr2=l2
        head=None
        curr=head
        while curr1 and curr2:
            if curr==None:
                head=curr=ListNode()
            else:
                curr.next=ListNode()
                curr=curr.next

            sum=curr1.val+curr2.val+carry
            carry=0
            if sum>9:
                carry=sum//10
                sum=sum%10
            
            curr1=curr1.next
            curr2=curr2.next            
            curr.val=sum

        
        while curr1:
            curr.next=ListNode()
            curr=curr.next
            
            sum=curr1.val+carry
            carry=0
            if sum>9:
                carry=sum//10
                sum%=10
            
            curr.val=sum
            curr1=curr1.next

        while curr2:
            curr.next=ListNode()
            curr=curr.next
            
            sum=curr2.val+carry
            carry=0
            if sum>9:
                carry=sum//10
                sum%=10
            
            curr.val=sum
            curr2=curr2.next
        
        if carry>0:
            curr.next=ListNode(carry)
        
        return head
        
