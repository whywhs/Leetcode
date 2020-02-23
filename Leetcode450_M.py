# 删除二叉搜索树中的节点。采用了递归的做法，即分别根据key值的大小来对左右侧进行查找。找到值之后，如果不是一个完全的二叉树，则可以直接返回之后的值。
# 如果是一个完全的二叉树，则将二叉树与右子树的最后一个左值进行交换，然后再对这个key进一步查找，直到满足了上面的条件。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.right or not root.left:
                root = root.left or root.right
                return root
            else:
                right = root.right
                while(right.left):
                    right = right.left
                root.val,right.val = right.val,root.val
                root.right = self.deleteNode(root.right,key)

        return root
