# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the middle of the linked list
        slow = head
        fast = head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse the second list portion
        prev = None 
        curr = slow.next
        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp 
        slow.next = None
        #merge the lists 
        list1 = head 
        list2 = prev 
        while list2:
            tmp = list1.next
            list1.next = list2
            list1 = list2
            list2 = tmp
        return head
        
            
            
            
        
        
    