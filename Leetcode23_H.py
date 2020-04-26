# 合并K个排序链表。这个题目一次写出来了，用的分治算法。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return []
        if len(lists)==1:
            return lists[0]
        len_l = len(lists)
        mid = len_l//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        if not left or not right:
            return left or right
        if left.val>right.val:
            left,right = right,left
        head_l,head_r = left,right
        while(head_l and head_r):
            while(head_l and head_r and head_l.val<=head_r.val):
                pre = head_l
                head_l = head_l.next
            pre.next = head_r
            while(head_l and head_r and head_l.val>head_r.val):
                pre = head_r
                head_r = head_r.next
            pre.next = head_l
        pre.next = head_l if head_l else head_r
        return left