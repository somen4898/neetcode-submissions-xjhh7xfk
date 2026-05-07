# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        if not head or not head.next :
            return head
        while head :
            temp = head.next
            head.next = node
            node = head
            head = temp
        return node 
    
            