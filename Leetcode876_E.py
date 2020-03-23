# 链表的中间节点。这个题目是个easy，很容易想到的就是统计长度然后输出。但是这个题的好的解法就是快慢指针。
# 快慢指针是链表中非常需要注意的一个问题，还可以用来判断环形链表。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast = head,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow
        # s,count = head,0
        # while(s):
        #     count += 1
        #     s = s.next
        # mid = count//2
        # for i in range(mid):
        #     head = head.next
        # return head