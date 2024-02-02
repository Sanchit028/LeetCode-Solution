# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1=headA
        p2=headB
        c1=0
        c2=0
        while(p1 !=None and p2!=None):
            if p1==p2:
                print("Intersected at '",p1.val,"'")
                return p1
            if p1.next==None and c1==0:
                c1+=1
                p1=headB
            else:
                p1=p1.next
            if p2.next==None and c2==0:
                c2+=1
                p2=headA
            else:
                p2=p2.next
        print("NO intersection")
        return
