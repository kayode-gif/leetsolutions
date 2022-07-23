# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #case if first element in linked list needs removal 
        while head != None and head.val == val:
            #pointing removed head to next element
            head = head.next
        curr = head
        #if the next value in head list is not empty
        while curr and curr.next != None:
            #if next val is val
            if curr.next.val == val:
                #point it else where to next next
                curr.next = curr.next.next
            else:
                # shift it mun
                curr = curr.next
        return head