# 最长有效括号的长度。 第一种方法是动态规划的方法，具体做法就是。首先如果s[i]是')' 那么分为两种情况，第一种s[i-1]是'('，那么直接就可以和前面
# 一个字符组成一个有效括号。则res[i] = res[i-2]+2即可。 如果前面一个是')'，那么就要去向前看更远。首先，需要看到i-res[i-1]-1是否是'('，如果是
# 就可以组成一个更大的括号。 组成更大的括号，那么res[i] = res[i-1]+res[i-res[i-1]-2]+2，相当于就可以连接i-res[i-1]-2 到res[i-1]这一段的
# 有效括号了，同时还要加上2，因为又多了一个大括号。
# 另外一种方法就是采用了左右计数法。 首先从左往右遍历，如果遇到(，那么left+1。 如果遇到)，那么right+1。 从左往右遍历的话，如果right一旦大于left
# 就直接终止。 这样可以算出以(为标准计算的结果。 那么同样的，从右往左计算，可以得到以右括号为标准的结果。
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s: return 0
        # res = [0]*len(s)
        # for i in range(1,len(s)):
        #     if s[i]==')':
        #         if s[i-1]=='(':
        #             res[i] = res[i-2]+2
        #         else:
        #             if i-res[i-1]-1>=0 and s[i-res[i-1]-1]=='(':
        #                 res[i] = res[i-1]+res[i-res[i-1]-2]+2
        # return max(res)

        left,right,max_len=0,0,0
        for i in range(len(s)):
            if left<right:
                left,right = 0,0
            if s[i]=='(': left += 1
            else: right += 1
            if left == right and 2*left>max_len:
                max_len = 2*left
        
        left,right = 0,0
        s = s[::-1]
        for j in range(len(s)):
            if right<left:
                left,right = 0,0
            if s[j]=='(': left += 1
            else: right += 1
            if left==right and 2*left>max_len:
                max_len = 2*left
        return max_len
            