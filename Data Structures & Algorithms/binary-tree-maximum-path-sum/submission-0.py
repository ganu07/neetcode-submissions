# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [float('-inf')]
        def max_sum(root):
            if not root:
                return 0
            
            left = max(max_sum(root.left), 0)
            right = max(max_sum(root.right), 0)
            maxsum[0] = max(maxsum[0], left + right + root.val)
            return root.val + max(left, right)
        max_sum(root)
        return maxsum[0]
        