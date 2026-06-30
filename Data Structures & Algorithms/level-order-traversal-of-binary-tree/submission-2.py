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
        q = deque([root])
        output = []

        while q:
            current_len = len(q)
            current_level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                current_level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            output.append(current_level_nodes)
        
        return output