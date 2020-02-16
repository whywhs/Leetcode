#基本计算器。只包括（）和+-四种。做法和之前的II类似，但是要先去括号。
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return s
        num="0123456789"
        a = 0
        num_list=[]
        num_o=[]
        for i in s:
            if i == " ":
                continue
            elif i in "()":
                num_o.append(i)
            else:
                if i in num:
                    a = a*10+int(i)
                else:
                    num_list.append(a)
                    num_o.append(i)
                    a = 0
        num_list.append(a)

        len_o = len(num_o)
        test = []
        flag = 0
        dict_re = {"+":"-","-":"+","(":"(",")":")","w":"w"}
        for i in range(len_o):
            if num_o[i]==")":
                test.append("w")
                k=i
                while(test[k]!="("):
                    k=k-1
                test[k]="w"
                if k>0 and test[k-1]=="-":
                    for j in range(k,i+1):
                        test[j]=dict_re[test[j]]
            else:
                test.append(num_o[i])
        
        result=[num_list[0]]
        num_list.pop(0)
        for i in test:
            if i=="w":
                continue
            elif i=="+":
                result.append(num_list.pop(0))
            else:
                result.append(-num_list.pop(0))
        
        sum_all=0
        for sub in result:
            sum_all+=sub
        return sum_all 
