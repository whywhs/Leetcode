# 排序链表。这个用了一个二分法来解决。关键的就在于左右链表的划分问题，需要用一个while循环来进行，而不能像list一样直接进行检索。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = 0
        start = head
        while(start):
            num +=1 
            start = start.next
        return self.sort(head,num)

    def sort(self,head,num):
        if num<=1:
            return head
        start = head
        mid = num//2
        while(mid-1):
            start = start.next
            mid -= 1
        right = start.next
        start.next = None
        l = self.sort(head,num//2)
        r = self.sort(right,num-num//2)
        if l.val>r.val:
            l,r = r,l
        res = l
        res1 = res
        l = l.next
        while(l and r):
            while(l and r and l.val>r.val):
                res1.next = r
                res1 = res1.next
                r = r.next
            while(l and r and l.val<=r.val):
                res1.next = l
                res1 = res1.next
                l = l.next
        res1.next = l if l else r
        return res
