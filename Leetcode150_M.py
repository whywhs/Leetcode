#逆波兰表达式。使用栈很好求解，需要注意的一点是list查找比dict查找慢，使用dict查找才可以通过。
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)<=1:
            return int(tokens[0])
        result=[]
        len_t = len(tokens)
        dict_o = {"+":0,"-":0,"*":0,"/":0}
        for i in range(len_t):
            if tokens[i] not in dict_o:
                result.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    result[-2] = result[-2]+result[-1]
                elif tokens[i] == "-":
                    result[-2] = result[-2]-result[-1]
                elif tokens[i] == "*":
                    result[-2] = result[-2]*result[-1]
                else:
                    result[-2] = int(result[-2]/result[-1])
                result.pop(-1)
        return result[0]
