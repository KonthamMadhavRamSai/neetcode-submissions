# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def similar(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            curr=p.val==q.val
            left=similar(p.left,q.left)
            right=similar(p.right,q.right)
            if curr and left and right:
                return True
            else:
                return False
        condn=similar(p,q)
        return condn