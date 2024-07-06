# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        curent =  head
        while curent:
            nxt = curent.next
            curent.next = first
            first = curent
            curent = nxt
        return first