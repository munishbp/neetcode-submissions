# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        current=l3

        carryover:int=0

        while l1 or l2 or carryover:
            if l1: 
                v1=l1.val
            else: 
                v1=0

            if l2: 
                v2=l2.val
            else:
                v2=0
            
            val=v1+v2+carryover
            carryover=val//10
            val=val%10
            current.next=ListNode(val)

            current=current.next
            if l1: 
                l1=l1.next
            else: 
                l1=None

            if l2: 
                l2=l2.next
            else:
                l2=None

        return l3.next


        