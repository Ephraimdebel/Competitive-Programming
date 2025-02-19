# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count+=1
        n = count//2
        curr = head
        while n > 0:
            curr = curr.next
            n-=1
        return curr