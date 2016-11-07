import sys

class Solution(object):

    def playerMove(self, n):
        '''
        Optimal Strategy is to pick a stone such that whatever the option your opponent picks .. you always get to pick the last stone!
        '''
        if n-3 > 3:
            n = n - 3
        else:
            if n - 2 > 3:
                n = n - 2
            else:
                'No choice but to pick'
                n = n - 1
        return n

    def canWinNim(self, n):

        if n == 1 or n == 2 or n == 3:
            return True

        if n % 4 == 0:
            return False
            
        while n >= 0:
            move1 = n % 4
            n = n - move1

            if n % 4 == 0:
                return True

            move2 = n % 4
            n = n - move2

            if n % 4 == 0:
                return False

if __name__ == "__main__":
    nimgame = Solution()
    print nimgame.canWinNim(int(sys.argv[1]))

   