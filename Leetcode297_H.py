# 二叉树的序列化与反序列化。使用前序遍历的方法。
# 前序遍历: 父节点 =》 左节点 =》 右节点
# 中序遍历：左节点 =》 父节点 =》 右节点
# 后序遍历：左节点 =》 右节点 =》 父节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        list_all = data.split(',')
        root = self.func(list_all)
        return root
        
        
    def func(self,list_all):
        val = list_all.pop(0)
        if val=='#':
            return None
        val_node = TreeNode(val)
        val_node.left = self.func(list_all)
        val_node.right = self.func(list_all)
        return val_node
