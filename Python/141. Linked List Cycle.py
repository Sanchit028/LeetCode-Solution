# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        TempNode= ListNode('abc')
        def cy(Node):

            if Node.val=='abc':
                
                return True
            elif Node.next == None:
                return False

            temp=Node.next
            Node.next=TempNode
            return cy(temp)
        return cy(head)
