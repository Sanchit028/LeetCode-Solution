class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        if root.left is not None:
            res += self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right is not None:
            res += self.inorderTraversal(root.right)
        return res
