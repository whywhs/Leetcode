1. 两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_all = {}
        for i in range(len(nums)):
            if target-nums[i] in dict_all:
                return [dict_all[target-nums[i]],i]
            dict_all[nums[i]] = i

2. 两数相加
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        res,flag = None,0
        while(l1 or l2):
            if not l1:
                num = l2.val
            elif not l2:
                num = l1.val
            else:
                num = l1.val+l2.val
            if flag==1:
                num +=1
            flag = 0
            if num>=10:
                num -= 10
                flag = 1
            now = ListNode(num)
            now.next = res
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            res = now
        if flag==1:
            new = ListNode(1)
            new.next = res
            res = new
        new = None
        while(res):
            res.next,res,new = new,res.next,res
        return new

3.



4.无重复字符的最长子串
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len,len_now = 1,1
        i,j = 0,1
        dict_all = {s[0]:1}
        while(i<j and j<len(s)):
            if s[j] in dict_all:
                if len_now > max_len:
                    max_len = len_now
                while(s[j] in dict_all):
                    dict_all.pop(s[i])
                    i += 1
                    len_now -= 1
            dict_all[s[j]] = 1
            j += 1
            len_now += 1
        return max_len if len_now<max_len else len_now


5. 最长回文子串
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def func(a,b):
            while(a>=0 and b<len(s) and s[a]==s[b]):
                a -= 1
                b += 1
            return a+1,b-1

        if len(s)<2:
            return s
        max_len = 0
        for i in range(1,len(s)):
            s1,e1 = func(i,i)
            if e1-s1+1>max_len:
                max_len = e1-s1+1
                res = s1
            s2,e2 = func(i-1,i)
            if e2-s2+1>max_len:
                max_len = e2-s2+1
                res = s2
        return s[res:res+max_len]


6. 整数反转
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        s = str(x)
        s = s[::-1]
        zero = 0
        while(s[zero]=='0'):
            zero += 1
        s = s[zero:]
        if s[-1]=='-':
            s = s[:len(s)-1]
            s = '-'+s
        return int(s) if -2**31<=int(s)<=2**31-1 else 0


7.字符串转换整数 (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        zero = 0
        while(zero<len(s) and s[zero]==' '):
            zero += 1
        s = s[zero:]
        if not s:
            return 0
        flag = 1
        if s[0] in '+-' or s[0].isdigit():
            if s[0] in '+-':
                if s[0] == '-':
                    flag = -1
                s = s[1:]
            digit = 0
            while(digit<len(s) and s[digit].isdigit()):
                digit += 1
            s = s[:digit]
            if not s:
                return 0
            if int(s)*flag>2**31-1: return 2**31-1
            elif int(s)*flag<-2**31: return -2**31
            return int(s)*flag
        return 0


8. 正则表达式匹配
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dict_all = {}
        def func(s,p):
            if not p and not s:
                return True
            elif not p:
                return False
            if (p,s) in dict_all:
                return dict_all[(p,s)]
            first = True if s and (p[0]==s[0] or p[0]=='.') else False
            if len(p)>1 and p[1]=='*':
                res = (first and func(s[1:],p)) or func(s,p[2:])
            else:
                res = func(s[1:],p[1:]) if first else False
            dict_all[(p,s)] = res
            return res
        
        return func(s,p)


9.盛最多水的容器
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_now = 0
        i,j = 0,len(height)-1
        while(i<j):
            if height[i]<=height[j]:
                now = height[i]*(j-i)
                if now>max_now:
                    max_now = now
                i += 1
            else:
                now = height[j]*(j-i)
                if now>max_now:
                    max_now = now
                j -= 1
        return max_now


10. 罗马数字转整数
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_all = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res,flag = 0,0
        for i in range(len(s)):
            if flag==1:
                flag = 0
                continue
            if s[i]=='I':
                if i+1<len(s) and s[i+1] in 'VX':
                    res += 4 if s[i+1]=='V' else 9
                    flag = 1
                else:
                    res += 1
            elif s[i]=='X':
                if i+1<len(s) and s[i+1] in 'LC':
                    res += 40 if s[i+1]=='L' else 90
                    flag = 1
                else:
                    res += 10
            elif s[i]=='C':
                if i+1<len(s) and s[i+1] in 'DM':
                    res += 400 if s[i+1]=='D' else 900
                    flag = 1
                else:
                    res += 100
            else:
                res += dict_all[s[i]]
        return res       

11.最长公共前缀
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def judge(idx):
            now = strs[0][:idx+1]
            return all([strs[i][:idx+1]==now for i in range(1,len(strs))])


        if not strs:
            return ''
        min_len = min([len(s) for s in strs])
        i,j = 0,min_len-1
        while(i<=j):
            mid = (i+j)//2
            if judge(mid):
                i = mid+1
            else:
                j = mid-1
        return strs[0][:i]


12.三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j,k = i+1,len(nums)-1
            while(j<k):
                now = nums[i]+nums[j]+nums[k]
                if now==0:
                    res.append([nums[i],nums[j],nums[k]])
                    while(j+1<len(nums) and nums[j+1]==nums[j]):
                        j += 1
                    j += 1
                elif now>0:
                    k -= 1
                else:
                    j += 1
        return res

13. 电话号码组合
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_all = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def func(digits):
            if not digits:
                return ['']
            now = digits[-1]
            res = func(digits[:len(digits)-1])
            res_now = []
            for i in res:
                for j in dict_all[now]:
                    res_now.append(i+j)
            return res_now
        if not digits:
            return []
        return func(digits)