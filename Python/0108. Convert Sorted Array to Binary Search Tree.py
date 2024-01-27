# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums=sorted(nums)
        def CRTree(arr):
            mid=len(arr)//2
            node= TreeNode(val=arr[mid])
            if arr[:mid] != []:
                node.left=CRTree(arr[:mid])
            if arr[mid+1:] != []:
                node.right=CRTree(arr[mid+1:])
            return node
        return CRTree(nums)
        
