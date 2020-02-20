# 删除链表中的节点。在你不知道上一个节点是什么的情况下，来删除当前节点。操作即将该节点变为下个节点。将下个节点的val给当前节点，并将下个节点的
# next也赋给当前节点。这样，相当于跳过了下个节点，同时把上个节点变成上个节点。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
