class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #Check rows
        for row in range(0,len(board)):
            already = []
            for col in range(0, len(board)):
                if board[row][col] != '.':
                    if board[row][col] in already:
                        return False
                    else:
                        already.append(board[row][col])

        #Check col
        for col in range(0,len(board)):
            already = []
            for row in range(0, len(board)):
                if board[row][col] != '.':
                    if board[row][col] in already:
                        return False
                    else:
                        already.append(board[row][col])

        #Check box
        rows = [[0,1,2],[3,4,5],[6,7,8]]
        cols = [[0,1,2],[3,4,5],[6,7,8]]

        for row in rows:
            for col in cols:
                for r in row:
                    already = []
                    for c in col:
                        #print r,c
                        if board[r][c] != '.':
                            if board[r][c] in already:
                                print r,c
                                return False
                            else: 
                                already.append(board[r][c])
                #print '\n'
        return True

print Solution().isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])