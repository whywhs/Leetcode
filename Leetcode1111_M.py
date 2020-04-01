# 有效括号的嵌套深度。这个题目给出的seq一定是一个有效括号，那么当分出来的A与B的长度一样时，一定是结果最小的。
# 所以，题目就变成了找到两个相同长度的A与B，那么就是A为奇数位，B为偶数位。结果就一定是正确的。
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        result = []
        for i in range(len(seq)):
            if seq[i]=="(":
                result += [0] if i%2==0 else [1]
            elif seq[i]==")":
                result += [1] if i%2==0 else [0]
        return result