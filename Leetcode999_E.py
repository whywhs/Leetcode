# 车的可用捕获量。 一次只能吃一个。
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        len_x = len(board)
        len_y = len(board[0])
        for i in range(len_x):
            for j in range(len_y):
                if board[i][j] == 'R':
                    loca  = [i,j]
                    break
        test1 = [board[i][loca[1]] for i in range(len_x)]
        test2 = board[loca[0]]
        test1_left,test1_right = test1[:loca[0]],test1[loca[0]+1:]
        test2_left,test2_right = test2[:loca[1]],test2[loca[1]+1:]
        count = 0
        for m in [test1_left[::-1],test1_right,test2_left[::-1],test2_right]:
            for i in m:
                if i=='p':
                    count += 1
                    break
                if i=='B':
                    break
        return count