# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next 

        left = 0
        right = len(nodes) - 1
        curr = head

        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            nodes[right].next = nodes[left]
            right -= 1
        
        
        if nodes:
            nodes[left].next = None 



