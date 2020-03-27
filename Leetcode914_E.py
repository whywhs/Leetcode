# 卡牌分组。这个题目就是求数组内的最大公约数。
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        pre = 0
        for i in set(deck):
            now = deck.count(i)
            if pre==0:
                pre = now
                continue
            if pre>now:
                pre,now = now,pre
            while(now%pre!=0):
                now,pre = pre,now%pre
        if pre!=1:
            return True
        return False