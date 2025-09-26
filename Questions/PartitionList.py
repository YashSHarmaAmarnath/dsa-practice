# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = []
        after = []
        dummy = head

        while dummy:
            nxt_node = dummy.next
            dummy.next = None
            if dummy.val>=x:
                after.append(dummy)
            else:
                before.append(dummy)
            dummy = nxt_node
        
        Nhead = None
        dummy = None
        for node in before+after:
            if not Nhead:
                Nhead = node
                dummy = Nhead
            else:
                dummy.next = node
                dummy = dummy.next
        return Nhead

        # if before:
        #     head = before[0]
        #     dummy = head
        #     for node in before[1:]:
        #         dummy.next = node
        #         dummy = dummy.next
        # if after:
        #     if not head:
        #         head = after[0]
        #         dummy = head
        #         after = after[1:]
        #     for node in after:
        #         dummy.next = node
        #         dummy = dummy.next
        # dummy.next = None
        # return head

            
