# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2=list2.next
            head = head.next 
        while list1 != None:
            head.next = ListNode(list1.val)
            head=head.next 
            list1=list1.next 
        while list2 != None:
            head.next = ListNode(list2.val)
            head=head.next
            list2=list2.next 
        return res.next
        

            