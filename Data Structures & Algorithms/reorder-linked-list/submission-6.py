# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        new_list = ListNode()
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second_list = slow.next
        slow.next = None
        
        prev = None
        curr = second_list
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        
        second = prev
        first = head
        
        while first and second:
            new_list.next = first
            first = first.next
            new_list = new_list.next
            
            
            new_list.next = second
            second = second.next
            new_list = new_list.next
        
        if first:
            new_list.next = first
        
        if second:
            
            new_list.next = second
        