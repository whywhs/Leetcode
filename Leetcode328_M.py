# 奇偶链表。这个就是在图上画一下就可以做出来了。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        list_h = head
        list_h1 = head.next
        pre = head.next
        while(list_h.next and list_h1.next):
            list_h.next = list_h.next.next
            list_h = list_h.next
            list_h1.next = list_h1.next.next
            list_h1 = list_h1.next
                    
        list_h.next = pre
        
        return head
