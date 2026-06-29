# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr= head
        slow = fast = curr 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        next_node = slow.next
        slow.next = None

        prev= None
        second_head = next_node

        while second_head:
            next_node = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = next_node
        
        
        new = dummy = ListNode()
        first, second = head, prev
        while first and second:
            new.next = first
            first = first.next
            new = new.next

            new.next = second
            second = second.next
            new = new.next
        
        if first:
            new.next = first
        
        if second:
            new.next = second
        



        
        