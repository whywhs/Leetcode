# 拼写单词。这个题目其实比较简单，但我的做法复杂了，我的做法是先将单词和字典进行sorted，然后再对sorted之后的进行pop
# 通过比较pop的单词，来判断能否组成。 
# 比较官方的做法就是通过count来进行计数，如果单词中count的数目小于char中的，那么就一定可以组成。这里需要学习到的一个解法
# 是for else方法。 for else方法的执行步骤是先执行for循环，如果for循环没有被break，那么执行else循环，否则不执行。
# 然后就是python的参数传递问题：对于python来说，是没有办法来选择值传递还是地址传递的。默认情况下，对于可变的对象来说，如list
# dict等，这些相当于地址传递，是可以修改原始的值的。但是对于不可变对象来说，如tuple,str等，就是不能够改变原始值的，相当于是
# 值传递。 然后sorted是会新建一个存储空间，而list.sort是在原始list上进行的。
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dict_char = {}
        for i in set(chars):
            dict_char[i] = chars.count(i)

        len_r = 0
        for i in words:
            for j in set(i):
                if j not in dict_char or i.count(j) > dict_char[j]:
                    break
            else:
                len_r += len(i)
        return len_r

        """
        len_r = 0
        for i in words:
            if self.func(i,chars):
                len_r += len(i)
        return len_r
        
    def func(self,words,chars):
        words = sorted(words)
        chars = sorted(chars)
        k,l = 1,0
        while(chars!=[]):
            if k==len(words)+1:
                return True
            now = chars.pop()
            if now == words[-k]:
                k+=1
        if k==len(words)+1:
            return True
        return False
        """