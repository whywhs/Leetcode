# 朋友圈。这个题目首先定义了一个visit数组来记录有哪些人已经被访问过了，如果被访问过就可以跳过。 同时，当没有访问的时候，就一直将该人的朋友加入
# 朋友圈，直到没有可以加入的为止。
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        res,visit = 0,set()
        for i in range(n):
            if i not in visit:
                sub = [i]
                while(sub):
                    now = sub.pop()
                    for people in range(n):
                        if M[now][people] and people not in visit:
                            visit.add(people)
                            sub.append(people)
                res += 1
        return res
 