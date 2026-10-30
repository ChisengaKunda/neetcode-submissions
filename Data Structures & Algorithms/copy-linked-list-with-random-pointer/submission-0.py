"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head 

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next 
            
        curr = head 
        copy_head = Node(-1)
        c = copy_head

        while curr:
            c.next = nodes[curr]
            c.next.random = nodes[curr.random] if curr.random else None
            c = c.next 
            curr = curr.next 
        return copy_head.next


