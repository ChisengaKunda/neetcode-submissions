# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head 

        while curr:
            length += 1 
            curr = curr.next 

        target = length - n 
        curr = head 
        count = 0

        if target == 0:
            return head.next 

        while curr:
            count += 1 
            if count == target:
                curr.next = curr.next.next 
            else:
                curr = curr.next 
        return head 

