# 生命游戏。 这个题目又是一个图的遍历。
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == [] or board==[[]]:
            return board
        len_x = len(board)
        len_y = len(board[0])
        dict_r = {}
        for i in range(len_x):
            for j in range(len_y):
                count = self.find(i,j,len_x,len_y,board)
                if board[i][j] == 0 and count == 3:
                    dict_r[(i,j)] = 1
                    continue
                if board[i][j] == 1 and (count<2 or count>3):
                    dict_r[(i,j)] = 0
                    continue
                dict_r[(i,j)] = board[i][j]
        for i in dict_r:
            board[i[0]][i[1]] = dict_r[i]

    def find(self,x,y,len_x,len_y,board):
        result = 0
        dict_f = {}
        r1 = [max(x-1,0),y]
        r2 = [min(x+1,len_x-1),y]
        r3 = [x,max(y-1,0)]
        r4 = [x,min(y+1,len_y-1)]
        r5 = [max(x-1,0),max(y-1,0)]
        r6 = [max(x-1,0),min(y+1,len_y-1)]
        r7 = [min(x+1,len_x-1),max(y-1,0)]
        r8 = [min(x+1,len_x-1),min(y+1,len_y-1)]
        for i in [r1,r2,r3,r4,r5,r6,r7,r8]:
            if i==[x,y]:
                continue
            if board[i[0]][i[1]]==1 and tuple(i) not in dict_f:
                result += 1
                dict_f[tuple(i)] = 1
        return result