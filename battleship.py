class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
    
        previous = None
        horizontal = None
        vertical = None
        count = 0

        for rows in board:
            if not previous:
                for i in range(len(rows)):
                    if rows[i] != '.':
                        if row[i - 1] != '.':
                            horizontal = True 
            else:
                for i in range(len(rows)):
                    if horizontal:

            previous = rows 