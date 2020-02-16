class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return s
        num = "0123456789"
        a=0
        list_num = []
        list_o = []
        for i in s:
            if i==" ":
                continue
            if i in num:
                a = a*10+int(i)
            else:
                list_o.append(i)
                list_num.append(a)
                a=0
        list_num.append(a)
        result=[list_num[0]]
        for i in range(1,len(list_num)):
            if list_o[i-1] == "+":
                result.append(list_num[i])
            elif list_o[i-1] == "-":
                result.append(-list_num[i])
            elif list_o[i-1]== "*":
                result[-1] = result[-1]*list_num[i]
            else:
                result[-1] = int(result[-1]/float(list_num[i]))
        #print(result)
        sum_all = 0
        for i in result:
            sum_all+=i
        return sum_all
    
