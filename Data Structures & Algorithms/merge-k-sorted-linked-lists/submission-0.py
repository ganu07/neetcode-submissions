# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(l1, l2):
            first = l1
            second = l2
            merged_list = ListNode(0)
            dummy = merged_list

            while first and second:
                if first.val <= second.val:
                    dummy.next = first
                    first = first.next
                else:
                    dummy.next = second
                    second = second.next
                dummy = dummy.next

            dummy.next = first if first else second
        
            return merged_list.next
        
        while len(lists) > 1:
            new_list =[]
            i =0
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                new_list.append(merge(l1,l2))
                i = i + 2
            lists = new_list
        return lists[0]






