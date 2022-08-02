# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create a dummy node to have "n" gap
        dummy = ListNode(47,head)
        left = dummy
        # loop to place right pointer at n gap 
        right = head
        while n > 0:
            right = right.next
            n = n -1 
        # traverse list to when right and left is at desired n gap 
        while right:
            right = right.next
            left = left. next 
        #delete so point prev to next.next
        left.next = left.next.next
        
        return dummy.next