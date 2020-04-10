# 单词搜索。 这个题目是通过深度优先搜索来完成的。这个题目比较好的一点就是在每次执行完当前的DFS后，会对board中的元素进行还原
# 做法就是在dfs后，下面将之前记录的tmp值重新赋给board[x][y]，而且题目中使用''来记录运行过的地方也是很不错的想法， 可以
# 避免使用dict进行。
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board==[]:
            return False
        len_x,len_y = len(board),len(board[0])
        for i in range(len_x):
            for j in range(len_y):
                if self.func(i,j,len_x,len_y,0,board,word):
                    return True
        return False

    def func(self,x,y,len_x,len_y,k,board,word):
        if x<0 or x>=len_x or y<0 or y>=len_y or board[x][y]!=word[k]:
            return False
        if k==len(word)-1:
            return True
        tmp,board[x][y] = board[x][y],''
        res = self.func(x-1,y,len_x,len_y,k+1,board,word) or self.func(x,y-1,len_x,len_y,k+1,board,word) or self.func(x+1,y,len_x,len_y,k+1,board,word) or self.func(x,y+1,len_x,len_y,k+1,board,word)
        board[x][y] = tmp
        return res