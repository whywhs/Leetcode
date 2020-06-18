# 括号的分数。这个题目用的是栈的方法。当是'('时，我就append到stack中，当是')'时，那么我就首先判断是否最后一位为数字，如果是数字的话，
# 那么就累加，直到找到了上一个'('为止。 而如果上一个直接就是'('，那么就append(1)即可。
# 另外，最后的结果需要的是求和而不是返回首位。
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            if i=='(':
                stack.append(i)
            else:
                sub = 0
                while(stack[-1]!='('):
                    sub += stack.pop()
                stack.pop()
                if sub==0:
                    stack.append(1)
                else:
                    stack.append(sub*2)
        return sum(stack)