# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        arr = []       
        while dummy:
            # n+=1
            arr.append(dummy.val)
            dummy = dummy.next
        arr.sort()
        dummy = head
        i = 0
        while dummy:
            dummy.val = arr[i]
            i+=1
            dummy = dummy.next
        return head
