# 两数相加。 这个题目是一个链表的题目，其实我写的复杂了，因为拆分成两步来进行了，一步也是可以直接完成的。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
            
        l3_p = ListNode(1)
        l3_a = l3_p
        while(l1 and l2):
            val = l1.val+l2.val
            l3 = ListNode(val)
            l3_a.next = l3
            l3_a = l3_a.next
            l1 = l1.next
            l2 = l2.next   
        if l1 or l2:
            l3_a.next = l1 or l2

        sum_l = l3_p.next
        while(sum_l):
            if sum_l.val >= 10:
                sum_l.val = sum_l.val -10
                if not sum_l.next:
                    sum_l.next = ListNode(1)
                    break
                sum_l.next.val = sum_l.next.val+1
            sum_l = sum_l.next
        
        return l3_p.next