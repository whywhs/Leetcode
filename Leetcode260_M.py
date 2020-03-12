# 只出现一次的数字III。这个是要求在所有出现两次的数字中，找到两个出现了一次的数字。
# 这个题目的思路很巧妙，首先按之前的方法全部异或一遍，然后找到异或后的数的最高位，在bin()中，默认是从1开始的，即0b110。所以，该结果的第一位即1.
# 然后该结果的1肯定代表了在数组中存在的两个只出现1次的数字，在该位上一定是相异的。所以就可以对所有数组进行划分，其中一部分是该位1另一部分是0.
# 最后对数组的元素分别进行异或即可。
# 这个题目需要注意的地方在位运算上，>>是移位，bin是获得二进制，结果是0b11这种，类型均为str.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums[0]
        for i in nums[1:]:
            a = a^i
        n = len(bin(a))-3
        a,b = 0,0
        for i in nums:
            j = i>>n
            if bin(j)[-1]=='1':
                a = a^i
            else:
                b = b^i
        return a,b
