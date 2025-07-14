# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        n = 0
        dummy = head
        while dummy:
            dummy=dummy.next
            n+=1
        dummy = head
        while dummy:
            res+=dummy.val*(2**(n-1))
            n-=1
            dummy = dummy.next
        return res
