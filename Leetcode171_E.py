#Excel表格。相当于就是一个二十六进制转换，这里面唯一需要注意的就是，ord("a")获取ASCII码，chr(97)获取ASCII码的表达值。
#class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i in s:
            num = ord(i)-ord("A")+1
            a = a*26+num
        return a
