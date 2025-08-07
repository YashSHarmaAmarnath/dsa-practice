# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return None
        odd = []
        even = []
        dummy = head
        i = 1
        while dummy:
            if i%2==0:
                even.append(dummy)
            else:
                odd.append(dummy)
            dummy = dummy.next
            i+=1
        # if odd:
        for i in range(len(odd)-1):
            odd[i].next = odd[i+1]
        if even:
            odd[-1].next = even[0]
            for i in range(len(even)-1):
                even[i].next = even[i+1]
            even[-1].next = None
        else:
            odd[-1].next = None
        return head

        
