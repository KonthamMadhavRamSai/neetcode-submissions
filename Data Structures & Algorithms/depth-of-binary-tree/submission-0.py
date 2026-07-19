# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def countdepth(root,count):
            if root is None:
                return count
            left=0
            if root.left:
                left=countdepth(root.left,count+1)
            right=0
            if root.right:
                right=countdepth(root.right,count+1)
            return max(left,right,count+1)
        return countdepth(root,0)

        