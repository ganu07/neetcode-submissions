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
            merged_list = ListNode(0)
            dummy = merged_list
            
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                
                dummy = dummy.next
            
            dummy.next = l1 if l1 else l2
            return merged_list.next
        
        while len(lists)>1:
            i = 0
            new_list = []
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                new_list.append(merge(l1, l2))
                i += 2
            lists = new_list 
        
        return lists[0]






