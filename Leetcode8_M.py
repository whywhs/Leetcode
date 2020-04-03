# 字符串转换整数。 这个题目需要学习的一个东西即str.lstrip()，对字符串前后的空格进行去除。
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max,int_min = 2**31-1,-2**31
        str_trans = str.lstrip()
        if str_trans == '': return 0
        str_num = '0123456789'
        flag = 1
        if str_trans[0] in '+-':
            if str_trans[0] == "-": flag = -1
            str_trans = str_trans[1:]
        result = []
        for i in str_trans:
            if i in str_num:
                result += [i]
            else: break
        if result == []:
            return 0
        out = int("".join(result))*flag
        if out>int_max or out<int_min:    
            return int_max if out>0 else int_min
        return out