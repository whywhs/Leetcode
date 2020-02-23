# 二叉搜索树迭代器。下面的是笨方法，即先将二叉搜索树进行中序遍历，得到数列，再进行输出。
# 简单的方法是直接对二叉搜索树所有左边的树append到result上，注意是节点append上去。然后再判断有没有右节点，再依次append并输出。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.result = []
        while(root):
            self.result.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        root_now = self.result.pop(-1)
        new = root_now.right
        if new:
            while(new):
                self.result.append(new)
                new = new.left
        return root_now.val
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.result)>0:
            return True
        return False
        
    

# class BSTIterator(object):

#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.result = self.my_list(root)

#     def next(self):
#         """
#         @return the next smallest number
#         :rtype: int
#         """
#         return self.result.pop(0)
            
            

#     def hasNext(self):
#         """
#         @return whether we have a next smallest number
#         :rtype: bool
#         """
#         if len(self.result)>0:
#             return True
#         return False
        
    
#     def my_list(self,root):
#         if not root :
#             return []
#         if not root.left and not root.right:
#             return [root.val]
#         else:
#             result_left = self.my_list(root.left)
#             result_right = self.my_list(root.right)
#             result = result_left+[root.val]+result_right
#         return result



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
