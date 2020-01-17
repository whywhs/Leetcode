#单词拆分，动态规划的思想，第i个位置的值需要由以下条件来进行判断（1、dp[:i]在worddict中 2、dp[:j]为1且dp[j,i]在worddict中）
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        flag = []
        result = [0]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                result[i]=1
                flag.append(i)
            else:
                for j in flag:
                    if s[j+1:i+1] in wordDict:
                        result[i]=1
                        flag.append(i)
                        break
        if result[-1]==1:
            return True
        return False
