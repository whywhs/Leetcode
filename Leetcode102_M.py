# 二叉树的层序遍历。这个题目是经典的问题，有两种思路，第一种就是用循环的方法，创建一个tree数组，将每一层依次加入到tree中，在这种方法里
# 需要注意到的一个问题就是将sub替换为tree的时候，即下一层的节点替换当前层的时候，不可以用tree=sub，这个是一个浅拷贝，会出错。而应该
# 使用tree+=sub，因为两个list相加是O(n+k)的复杂度，相当于遍历了数组并赋值。
# 这种方法空间上使用较多，另外有一个比较好的方法是通过引入level的方法。level来记录当前是第几层了，这样就可以知道应该在第几层加入val.
# 那么就相当于在递归的时候，需要维护level和res还有root.其中当level与res的长度相等的时候，证明应该在res中加入一个新的[]，因为当前
# 需要append进来的是res中第level个。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        return self.func(0,[],root)

    def func(self,level,res,root):
        if len(res)==level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            res = self.func(level+1,res,root.left)
        if root.right:
            res = self.func(level+1,res,root.right)
        return res