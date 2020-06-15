# 最长公共前缀。这个题目有两种方法吧，一个是用字典树，另外一个用二分。使用二分的思路就是，首先找到序列中最短的那一个项，然后以该最短项长度为
# 二分的起始边界，求出mid。 对所有的str进行mid的匹配，当所有的都匹配上了，那么i=mid+1，如果有不匹配上的那么j=mid。 这个算法时间复杂度
# O(mnlogm). 不用切片进行比较的话空间复杂度也应该是O(N)，因为最开始进行比较的时候，构建了长度数组

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        len_s = min([len(s) for s in strs])
        i,j = 0,len_s
        while(i<j):
            mid = (i+j)//2
            sub = strs[0][:mid+1]
            for m in strs[1:]:
                if sub!=m[:mid+1]:
                    j = mid
                    break
            if j!=mid: i = mid+1
        return strs[0][:j]
        


        # if not strs: return ''
        # dict_all = {}
        # tree = dict_all
        # for i in strs[0]:
        #     tree = tree.setdefault(i,{})
        # tree['end']=True

        # res_all = strs[0]
        # for j in strs[1:]:
        #     tree,res = dict_all,''
        #     for k in j:
        #         if k in tree:
        #             res += k
        #             tree = tree[k]
        #         else: break
        #     if len(res)<len(res_all):
        #         res_all = res
        # return res_all