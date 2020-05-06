# 栈的压入、弹出序列。 这个题目可以用模拟的方法来做。具体的做法就是用stack来模拟一个栈。然后res和ori分别模拟能够得到的output和给出的
# 如果两个相同就可以得到。注意最后要清空stack和popped，因为当末尾不同时，res和ori都不再更新。
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack,ori,res = [],[],[]
        while(pushed):
            stack.append(pushed.pop(0))
            while(stack and popped and stack[-1] == popped[0]):
                res.append(stack.pop())
                ori.append(popped.pop(0))
        res += stack[::-1]
        ori += popped
        return res==ori

# 这个代码更简洁。相当于判断最后stack能不能pop到空作为是否为True的标记
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack,pushed,k = [],pushed[::-1],0
        while(pushed):
            stack.append(pushed.pop())
            while(stack and stack[-1]==popped[k]):
                stack.pop()
                k += 1
        return not stack
