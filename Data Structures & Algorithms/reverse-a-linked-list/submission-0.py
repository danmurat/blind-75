# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.traverse(head, None)
        

    def traverse(self, current_node, previous_node) -> None:
        if current_node == None: # might not have a llist
            return
        if current_node.next == None:
            current_node.next = None if previous_node == None else previous_node
            return current_node
        else:
            next_node = current_node.next
            current_node.next = None if previous_node == None else previous_node
            return self.traverse(next_node, current_node)