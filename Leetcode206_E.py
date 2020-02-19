# 反转链表。两种方法，一种是递归式的反转，另外一种是将旧的链表去头，将新的链表加入去掉的头部。
# 递归式的反转是将头部一个一个往后移动，并将剩下的反转。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        list_h = head
        pre = None
        while(list_h.next):
            pre_old = pre
            pre = list_h.next
            list_h.next = list_h.next.next
            if pre_old:
                pre.next = pre_old
            else:
                pre.next = list_h
        return pre

    
        list_h = head
        new = None
        while(list_h):
            pre = list_h.next
            list_h.next = new
            new = list_h
            list_h = pre
        return new
            
