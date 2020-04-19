# 顺时针打印矩阵。这个题目简单的方法就是用矩阵的转置+倒序。
# 这里需要学习的方法就是python中的zip算法。zip(*num)就是对num进行解包。可以记成对num求转置。
# 但是题目需要打印的东西，应该在转置的基础上再加一个倒序，就可以了。
# 记住，zip在python2和3中是有不一样的用法。在2中返回的就是一个list，而在3中zip还需要进行一步list()
# 在3中，返回的是一个zip对象。而2中返回的是一个list()。
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while(matrix!=[]):
            res += matrix.pop(0)
            matrix = zip(*matrix)[::-1]
        return res
            
        