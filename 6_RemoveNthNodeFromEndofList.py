# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
# head.next=ListNode(2)
# head.next.next=ListNode(3)
# head.next.next.next=ListNode(4)
# head.next.next.next.next=ListNode(5)
n = 1
slow = head 
fast = head 

for i in range(n):
    fast=fast.next
while fast!=None:
    slow=slow.next
    fast=fast.next
slow.next = slow.next.next


    

