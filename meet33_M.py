# 二叉搜索树的后序遍历序列。这个题目利用了二叉搜索树和后序遍历的性质。对于二叉搜索树来说，左子树<root<右子树。而
# 对于后序遍历来说，root的值一定在末尾。所以，就可以先pop出root，那么剩下的就是左右子树，从左往右进行遍历，当
# 遍历到大于root值的idx时，就是左右子树的分界点。然后，对右子树所有值进行遍历，如果右子树遍历出来的数有比root
# 小的，说明一定不成立。反之继续递归左右子树。


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def func(postorder):
            if len(postorder)<=1:
                return True
            now = postorder.pop()
            flag = 0
            for i in range(len(postorder)):
                if flag==1 and postorder[i]<now:
                    return False
                if postorder[i]>now:
                    flag = 1
                    idx = i
            if flag==0 or (flag==1 and idx==len(postorder)-1):
                return func(postorder)
            return func(postorder[:idx]) and func(postorder[idx:])

        return func(postorder)