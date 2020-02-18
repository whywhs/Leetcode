#环形链表。环形链表的做法就是利用快慢指针，这对于求解是否有环是一个非常有效地方法。当快的指针能够追上慢的指针，说明有环。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_h = head
        list_h1 = head
        while(list_h and list_h1 and list_h1.next):
            if list_h.next==list_h1.next.next:
                return True
            list_h = list_h.next
            list_h1 = list_h1.next.next
        return False
