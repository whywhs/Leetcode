# 不同的二叉搜索树。这个题目属于比较巧妙的想法。对于n来说，我们设定G(n)为总的二叉搜索树个数。设定F(i,n)为以i为root的二叉搜索树个数。
# 则 G(n) = F(1,n)+F(2,n)+...+F(n,n) 又可以知道，F(i,n) = G(i-1)*G(n-i)即等于其左边的数目乘上右边的数目。所以，整个循环就可以确定下来了。
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0],G[1] = 1,1
        for i in range(2,n+1):
            for j in range(i):
                G[i] += G[j]*G[i-1-j]
        return G[-1]
