# 填充每个节点的下一个右侧节点指针II。这个题目相比于上面的一个题目改的地方在将完美二叉树变为了普通二叉树。使用之前的递归方法将比较困难，故使用了
# 层序遍历的做法。这个在空间复杂度上可能不满足要求。但是更容易写出来。
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        list_result=[root]
        while(list_result!=[]):
            list_sub = []
            len_l = len(list_result)
            for i in range(len_l):
                now = list_result[i]
                now.next = list_result[i+1] if i+1<len_l else None
                if now.left and now.right:
                    list_sub+=[now.left,now.right]
                elif now.left==None and now.right==None:
                    continue
                else:
                    list_sub+=[now.left or now.right]
            list_result = list_sub
            
        return root
