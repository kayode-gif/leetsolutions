# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        while l1 and l2:
            #if the value in l2 is less
            if l1.val > l2.val:
                #shift to next value in l2(so add it)
                curr.next = l2
                # move pointer
                l2 = l2.next
                
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        # if not any more values in l1, add remaining l2
        if not l1:
            curr.next = l2
            
        if not l2:
            curr.next = l1
        return dummy.next
                
        
        