# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # hashMap = {}
        dummy = head
        nodes = []
        while dummy:
            # hashMap[dummy.val] = dummy
            nodes.append(dummy)
            dummy = dummy.next
        dummy = ListNode(0)
        curr = dummy

        n = len(nodes)
        i = 0
        while i <n :
            if i + 1 < n:
                # Swap pair
                curr.next = nodes[i + 1]
                curr = curr.next
                curr.next = nodes[i]
                curr = curr.next
            else:
                # If one node left (odd length), no swap
                curr.next = nodes[i]
                curr = curr.next
            i += 2
        curr.next = None
        return dummy.next
