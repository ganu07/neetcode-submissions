# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            current_len = len(q)
            current_level_nodes = []
            for i in range(current_len):
                node = q.popleft()
                current_level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(current_level_nodes)
        
        return result
                
        
        