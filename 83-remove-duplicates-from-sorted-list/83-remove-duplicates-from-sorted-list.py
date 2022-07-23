# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set current to head
        curr = head
        # while head isnt none and next value isnt none
        while curr != None and curr.next != None:
            #if curr value is the same as next value 
            if curr.val == curr.next.val:
                #set curr value to next
                curr.next = curr.next.next 
            else:
                curr = curr.next
        return head
        