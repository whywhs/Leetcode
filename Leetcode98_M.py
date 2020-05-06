# 验证二叉搜索树。采用的是中序遍历的方法，中序遍历即先遍历节点左侧，再遍历节点，最后遍历节点右侧。则验证二叉搜索树的关键在于中序遍历的数组是否是
# 一个单调递增的数组，否则就不是二叉搜索树。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.my_list(root)
        print(result)
        if result==[]:
            return True
        else:
            for i in range(1,len(result)):
                if result[i]<=result[i-1]:
                    return False
            return True
        
        
    def my_list(self,root):
        if not root :
            return []
        else:
            result_left = self.my_list(root.left)
            result_right = self.my_list(root.right)
            result = result_left+[root.val]+result_right
        return result


# 这个是采用递归的一个解法，主要的思路就是要在每次递归的过程中维护一个上下界限。分别是最小值，以及最大值。
# 对于初始的root来说，最小值和最大值分别为inf和-inf
# 对于递归的left来说，最小值就是上一轮的min_v,最大值就是当前的root.val，这样是可以限定住所有的left都小于当前的root.val
# 因为root.val都是在min,max之间的，那么更新只会越来越小。
# 对于right也是同理。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.func(root,float('-inf'),float('inf'))
    def func(self,root,min_v,max_v):
        if not root:
            return True
        if min_v<root.val<max_v:
            return self.func(root.left,min_v,root.val) and self.func(root.right,root.val,max_v)
        return False


# 采用中序遍历来判断二叉搜索树。中序遍历就是先左后中后右，那么我每一次while循环中都首先append上所有的left，然后一个一个pop出来
# 则当前pop出来的值，就是当前的root，那么将当前root与pre相比，如果比pre小则一定不是。
# 如果比pre大，那么pre变为当前root的值，再将root.right append进去。
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res,pre = [],float('-inf')
        while(res or root):
            while(root):
                res.append(root)
                root = root.left
            now = res.pop()
            if now.val<=pre:
                return False
            pre = now.val
            root = now.right
        return True
