# 有序链表转换二叉搜索树。 记住，如果仅仅是找中点的话，完全可以直接用双指针来做。如果想要分开左右，那么就记录slow的上一个数，让其next为None
# 同时记录slow。则左半部分就是head，右半部分就是slow。 这样就可以将链表分开。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        fast,slow = head,head
        pre = None
        while(fast and fast.next):
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if not pre:
            return TreeNode(head.val)
        pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
