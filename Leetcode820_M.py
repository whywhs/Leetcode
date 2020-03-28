# 单词的压缩编码。这个题目标准做法应该就是字典树的做法。对于字典树来说，我是写了两个代码，一个是求字典树长度，另外一个是构造字典树。
# 在这里构造字典树有讲究，不能单纯的构建，而是应该对字典树进行判断，判断是否满足减免的条件。如果当前end不在，那么需要构建两个单词，
# 或者end在，但是当前node已经比1大了，说明不可能再去和之前的合并了。这里只需要大于1即可是因为end只会有一个，如果有多个说明有重复的
# 单词，那就不需要另行计算。
# 这个题目一个好的做法就是用类似堆的做法，通过对逆序字符进行sort()，这个sort是会按首字母开始，并按长度排序的。那么之后只需要判断
# 前面一个单词是不是后面一个单词的前缀即可。

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = list(set(words))
        if len(words)==1:
            return len(words[0])+1
        r_words = [i[::-1] for i in words]
        r_words.sort()
        result,num_words = 0,0
        while(len(r_words)>1):
            len_sub = len(r_words[-2])
            result += len(r_words[-1])
            if r_words[-1][:len_sub] == r_words[-2]:
                r_words.pop()
            r_words.pop()
            num_words += 1
        
        return result+len(r_words[0])+num_words+1 if r_words!=[] else result+num_words



    #     dict_tree,count = {},0
    #     for i in set(words):
    #         node = dict_tree
    #         len_sub = 0
    #         for j in i[::-1]:
    #             if j not in node and node!={}:
    #                 if "end" not in node or (len(node)>1 and "end" in node):
    #                     count += len_sub
    #             node = node.setdefault(j,{})
    #             len_sub += 1
    #         node["end"] = True
    #     len_all = self.find_len(dict_tree)
    #     return len_all+count
    
    # def find_len(self,dict_tree):
    #     if len(dict_tree)==1 and "end" in dict_tree:
    #         return 1
    #     len_sub = 0
    #     for i in dict_tree:
    #         if i=="end":
    #             continue
    #         len_sub += self.find_len(dict_tree[i])
    #         len_sub += 1
    #     return len_sub