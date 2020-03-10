# 单词接龙。这个题目是典型的广度优先搜索题目。值得学习的地方有两个，一个是双向BFS，另一个是set操作。
# 双向BFS。即从前往后，从后往前均进行BFS，当一方的BFS结果大于另一方，则改从小的一方继续进行。
# set操作。a={'ccc'}这个定义就是一个set变量。然后set是有len的操作，同时set的加是add，set的减是remove，set的update是迭代的加入变量。
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        if len(beginWord)==1:
            return 2
        count,result,result_e,sub = 1,{beginWord},{endWord},set()

        while(len(result)!=0):
            if len(result)>len(result_e):
                result,result_e = result_e,result
            for i in wordList:
                for j in result:
                    if self.judge(i,j):
                        if i in result_e:
                            return count+1
                        sub.add(i)
            result,sub = sub,set()
            count += 1
        return 0
                
        
    def judge(self,a,b):
        k = 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                k += 1
        if k!=1:
            return False
        return True
