# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        if root.left is not None:
            res += self.postorderTraversal(root.left)
        if root.right is not None:
            res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res
